from django.shortcuts import render

from app_main.models import (
    BorrowingRankStat,
    FavoriteCanteenStat,
    GraduatePersonalStat,
    LibraryBorrowingStat,
    OrderingRankStat,
    SportsCompetitionStat,
)
from django_cas_ng.decorators import login_required

# 毕业生总数
GRADUATE_TOTAL_NUM = -1
# 显示借阅量排名的阈值（前50%才显示）
SHOW_BORROWING_RANK_THRESHOLD = 0.5
# 最高借阅量
MAX_BORROWING_NUM = -1


@login_required
def personal_view(request):
    # 获取当前用户的一卡通号
    seu_card_id = request.user.username
    # # 非内测用户，显示提示信息
    # with open("./test_users.txt", "r") as f:
    #     test_users = f.read().splitlines()
    # if seu_card_id not in test_users:
    #     return render(request, "welcome_view.html", {"is_eligible": False})
    # 若不在毕业生数据中，则显示提示信息
    if (
        not GraduatePersonalStat.objects.only("seu_card_id")
        .filter(seu_card_id=seu_card_id)
        .exists()
    ):
        return render(request, "welcome_view.html", {"is_eligible": False})

    # 查询指定毕业生的个人统计信息
    graduate = GraduatePersonalStat.objects.get(seu_card_id=seu_card_id)

    # 毕业生总数
    global GRADUATE_TOTAL_NUM
    if GRADUATE_TOTAL_NUM == -1:
        GRADUATE_TOTAL_NUM = GraduatePersonalStat.objects.count()

    # 全校最高借阅量
    global MAX_BORROWING_NUM
    if MAX_BORROWING_NUM == -1:
        MAX_BORROWING_NUM = BorrowingRankStat.objects.order_by("borrowing_rank")[
            0
        ].borrowing_num

    # 最常去相同食堂的人数
    same_favorite_canteen_percent = get_favorite_canteen_percent(
        graduate.most_frequent_consumption_place
    )

    # 图书馆相关统计信息（借阅量排名、本学院借阅量第一名）
    show_borrowing_rank, borrowing_rank_percent, top_borrower_in_unit = (
        get_library_stat(graduate.total_borrowed_books_num, graduate.unit_name)
    )

    # 场馆预约次数排名
    gym_ordering_rank_percent = get_gym_stat(graduate.gym_ordered_times)

    # 体育竞赛信息
    show_sports_competitions, sports_competition = get_sports_competition_stat(
        seu_card_id
    )

    return render(
        request,
        "personal_view.html",
        {
            "graduate": graduate,
            "same_favorite_canteen_percent": same_favorite_canteen_percent,
            "show_borrowing_rank": show_borrowing_rank,
            "borrowing_rank_percent": borrowing_rank_percent,
            "max_total_borrowed_books_num": MAX_BORROWING_NUM,
            "top_borrower_in_unit": top_borrower_in_unit,
            "gym_ordering_rank_percent": gym_ordering_rank_percent,
            "show_sports_competitions": show_sports_competitions,
            "sports_competition": sports_competition,
        },
    )


def get_favorite_canteen_percent(most_frequent_consumption_place):
    """计算最常去相同食堂的人数百分比"""
    if not most_frequent_consumption_place:
        same_favorite_canteen_percent = "0.00%"
    else:
        same_favorite_canteen_cnt = FavoriteCanteenStat.objects.get(
            canteen_name=most_frequent_consumption_place
        ).count
        same_favorite_canteen_percent = (
            f"{same_favorite_canteen_cnt / GRADUATE_TOTAL_NUM:.2%}"
        )

    return same_favorite_canteen_percent


def get_library_stat(total_borrowed_books_num, unit_name):
    """计算图书馆相关统计信息（借阅量排名、本学院借阅量第一名）"""
    # 借阅量排名
    if not total_borrowed_books_num or int(total_borrowed_books_num) == 0:
        show_borrowing_rank = False
        borrowing_rank_percent = "0.00%"
    else:
        # 检查排名表中是否有该借阅量（处理两表数据未同步的情况）
        if (
            BorrowingRankStat.objects.only("borrowing_num")
            .filter(borrowing_num=total_borrowed_books_num)
            .exists()
        ):
            borrowing_rank = BorrowingRankStat.objects.get(
                borrowing_num=total_borrowed_books_num
            ).borrowing_rank
        # 若不存在则用最邻近的借阅量的排名代替
        else:
            borrowing_rank = (
                BorrowingRankStat.objects.filter(
                    borrowing_num__lt=total_borrowed_books_num
                )
                .order_by("-borrowing_num")[0]
                .borrowing_rank
            )
        # 判断是否显示借阅量排名并计算排名百分比
        show_borrowing_rank = (
            borrowing_rank / GRADUATE_TOTAL_NUM < SHOW_BORROWING_RANK_THRESHOLD
        )
        borrowing_rank_percent = f"{1 - (borrowing_rank - 1) / GRADUATE_TOTAL_NUM:.2%}"

    # 本学院借阅量第一名
    if (
        not unit_name
        or not LibraryBorrowingStat.objects.only("unit_name")
        .filter(unit_name=unit_name)
        .exists()
    ):
        top_borrower_in_unit = None
    else:
        top_borrower_in_unit = LibraryBorrowingStat.objects.filter(
            unit_name=unit_name
        ).order_by("rank")[0]

    return show_borrowing_rank, borrowing_rank_percent, top_borrower_in_unit


def get_gym_stat(gym_ordered_times):
    """计算体育场馆相关统计信息（场馆预约次数排名）"""
    # 预约次数排名
    if not gym_ordered_times or int(gym_ordered_times) == 0:
        ordering_rank_percent = "0.00%"
    else:
        # 检查排名表中是否有该预约次数（处理两表数据未同步的情况）
        if (
            OrderingRankStat.objects.only("ordering_times")
            .filter(ordering_times=gym_ordered_times)
            .exists()
        ):
            ordering_rank = OrderingRankStat.objects.get(
                ordering_times=gym_ordered_times
            ).ordering_rank
        # 若不存在则用最邻近的预约次数的排名代替
        else:
            ordering_rank = (
                OrderingRankStat.objects.filter(ordering_times__lt=gym_ordered_times)
                .order_by("-ordering_num")[0]
                .ordering_rank
            )
        # 计算排名百分比
        ordering_rank_percent = f"{1 - (ordering_rank - 1) / GRADUATE_TOTAL_NUM:.2%}"

    return ordering_rank_percent


def get_sports_competition_stat(seu_card_id):
    """获取体育竞赛信息"""
    sports_competition_list = SportsCompetitionStat.objects.filter(
        seu_card_id=seu_card_id
    )
    show_sports_competitions = bool(sports_competition_list)
    sports_competition = (
        sports_competition_list.order_by("?")[0] if show_sports_competitions else None
    )

    return show_sports_competitions, sports_competition
