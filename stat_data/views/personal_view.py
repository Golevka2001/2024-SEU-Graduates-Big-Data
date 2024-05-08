from django.shortcuts import redirect, render

from django_cas_ng.decorators import login_required
from stat_data.models import (
    FavoriteCanteenStat,
    GraduatePersonalStat,
    LibraryBorrowingStat,
    SportsCompetitionStat,
)

# 显示借阅量排名的阈值（前50%才显示）
SHOW_BORROWING_RANK_THRESHOLD = 0.5


@login_required
def personal_view(request):
    # 获取当前用户的一卡通号
    seu_card_id = request.user.username
    # 若不在毕业生数据中，则显示提示信息
    if not GraduatePersonalStat.objects.filter(seu_card_id=seu_card_id).exists():
        return redirect("error:not_eligible_view")

    # 查询指定毕业生的个人统计信息
    graduate = GraduatePersonalStat.objects.get(seu_card_id=seu_card_id)

    # 毕业生总数
    graduate_total_num = GraduatePersonalStat.objects.count()

    # 最常去相同食堂的人数
    if not graduate.most_frequent_consumption_place:
        same_favorite_canteen_percent = "0.00%"
    else:
        same_favorite_canteen_cnt = FavoriteCanteenStat.objects.get(
            canteen_name=graduate.most_frequent_consumption_place
        ).count
        same_favorite_canteen_percent = (
            f"{same_favorite_canteen_cnt / graduate_total_num:.2%}"
        )

    # 借阅量排名
    borrowing_rank = GraduatePersonalStat.objects.filter(
        total_borrowed_books_num=graduate.total_borrowed_books_num
    ).count()
    show_borrowing_rank = (
            borrowing_rank < graduate_total_num * SHOW_BORROWING_RANK_THRESHOLD
    )
    borrowing_rank_percent = f"{1 - borrowing_rank / graduate_total_num:.2%}"

    # 全校最高借阅量
    max_total_borrowed_books_num = (
        LibraryBorrowingStat.objects.extra(
            select={
                "total_borrowed_books_num_int": "CAST(total_borrowed_books_num AS SIGNED INTEGER)"
            }
        ).order_by("-total_borrowed_books_num_int")[0]
    ).total_borrowed_books_num

    # 本学院借阅量第一名
    if not graduate.unit_name:
        top_borrower_in_unit = None
    else:
        unit_name = graduate.unit_name
        same_unit_borrowers = (
            LibraryBorrowingStat.objects.filter(unit_name=unit_name)
            .extra(
                select={
                    "total_borrowed_books_num_int": "CAST(total_borrowed_books_num AS SIGNED INTEGER)"
                }
            )
            .order_by("-total_borrowed_books_num_int")
        )
        top_borrower_in_unit = same_unit_borrowers[0] if same_unit_borrowers else None

    # 场馆预约次数排名（gym_ordered_times）
    gym_ordering_rank = GraduatePersonalStat.objects.filter(
        gym_ordered_times=graduate.gym_ordered_times
    ).count()
    gym_ordering_rank_percent = f"{1 - gym_ordering_rank / graduate_total_num:.2%}"

    # 是否显示体育竞赛
    sports_competition_list = SportsCompetitionStat.objects.filter(
        seu_card_id=seu_card_id
    )
    show_sports_competitions = bool(sports_competition_list)
    sports_competition = (
        sports_competition_list[0] if show_sports_competitions else None
    )

    return render(
        request,
        "personal_view.html",
        {
            "graduate": graduate,
            "same_favorite_canteen_percent": same_favorite_canteen_percent,
            "show_borrowing_rank": show_borrowing_rank,
            "borrowing_rank_percent": borrowing_rank_percent,
            "max_total_borrowed_books_num": max_total_borrowed_books_num,
            "top_borrower_in_unit": top_borrower_in_unit,
            "gym_ordering_rank_percent": gym_ordering_rank_percent,
            "show_sports_competitions": show_sports_competitions,
            "sports_competition": sports_competition,
        },
    )
