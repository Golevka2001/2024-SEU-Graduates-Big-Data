import datetime

from django.shortcuts import render

from django_cas_ng.decorators import login_required
from stat_data.models import BirthDateStat, FavoriteCanteenStat, GraduatePersonalStat, LibraryBorrowingStat, OriginStat

# 只有借阅量排名在前 50% 的毕业生才会显示借阅量排名
SHOW_BORROWING_RANK_THRESHOLD = 0.5

# 只有场馆预约次数排名在前 50% 的毕业生才会显示场馆预约次数排名
SHOW_GYM_ORDERING_RANK_THRESHOLD = 0.5


@login_required
def personal_view(request):
    # 获取当前用户的一卡通号
    seu_card_id = request.user.username
    # TODO: 测试用，后续删除
    if seu_card_id == "TEST_USER":
        seu_card_id = "213216666"
    # 若不在毕业生数据中，则显示提示信息
    if not GraduatePersonalStat.objects.filter(seu_card_id=seu_card_id).exists():
        return render(request, "index.html", {"is_graduate": False})

    graduate = GraduatePersonalStat.objects.get(seu_card_id=seu_card_id)

    # 毕业生总人数（可以写成常量）
    # total_graduate_cnt = GraduatePersonalStat.objects.count()
    total_graduate_cnt = 123

    # 相同出生月日的毕业生人数
    birth_date = graduate.birth_date
    same_birth_date_cnt = BirthDateStat.objects.get(birth_date=birth_date).count - 1

    # 相同生源地的毕业生人数
    origin = graduate.origin
    same_origin_cnt = OriginStat.objects.get(origin=origin).count - 1

    # 流量相当于看了多少甄嬛传（按 167GB 计算）
    network_flow_equivalence = round(float(graduate.network_flow) / 167, 2)

    # 最常去相同食堂的人数
    same_favorite_canteen_cnt = FavoriteCanteenStat.objects.get(
        canteen_name=graduate.most_frequent_consumption_place).count - 1
    same_favorite_canteen_percent = f'{same_favorite_canteen_cnt / total_graduate_cnt:.2%}'

    # 是否显示最频繁同时、同地消费的人
    show_canteen_friend = bool(graduate.canteen_friend)

    # 是否显示论文
    show_papers = int(graduate.papers_num) > 0

    # 是否显示讲座
    show_lectures = bool(graduate.first_lecture_name)

    # 是否显示SRTP
    show_srtp_projects = float(graduate.srtp_score) > 0

    # 是否显示志愿活动
    show_volunteer_activities = float(graduate.volunteer_duration) > 0

    # 是否显示社会实践
    show_practice_projects = bool(graduate.first_practice_project_name)

    # 借阅量排名（total_borrowed_books_num）
    borrowing_rank = GraduatePersonalStat.objects.filter(
        total_borrowed_books_num__gt=graduate.total_borrowed_books_num).count()
    show_borrowing_rank = borrowing_rank < total_graduate_cnt * SHOW_BORROWING_RANK_THRESHOLD
    borrowing_rank_percent = f'{1 - borrowing_rank / total_graduate_cnt:.2%}'

    # 全校最高借阅量（可以写成常量）
    # max_total_borrowed_books_num = LibraryBorrowingStat.objects.order_by("-total_borrowed_books_num")[0]
    max_total_borrowed_books_num = 123

    # 本学院借阅量第一名
    unit_name = graduate.unit_name
    top_borrower_in_unit = \
        LibraryBorrowingStat.objects.filter(unit_name=unit_name).order_by("-total_borrowed_books_num")[0]

    # 是否显示借阅详情
    show_borrowing_detail = int(graduate.total_borrowed_books_num) > 0

    # 场馆预约次数排名（gym_ordered_times）
    gym_ordering_rank = GraduatePersonalStat.objects.filter(
        gym_ordered_times__gt=graduate.gym_ordered_times).count()
    show_gym_ordering_rank = gym_ordering_rank < total_graduate_cnt * SHOW_GYM_ORDERING_RANK_THRESHOLD
    gym_ordering_rank_percent = f'{1 - gym_ordering_rank / total_graduate_cnt:.2%}'

    # 在学校的第多少天
    days_in_seu = (datetime.date.today() - graduate.enroll_date).days

    return render(request, "personal_view.html", {"graduate": graduate,
                                                  "same_birth_date_cnt": same_birth_date_cnt,
                                                  "same_origin_cnt": same_origin_cnt,
                                                  "network_flow_equivalence": network_flow_equivalence,
                                                  "same_favorite_canteen_percent": same_favorite_canteen_percent,
                                                  "show_canteen_friend": show_canteen_friend,
                                                  "show_papers": show_papers,
                                                  "show_lecture": show_lectures,
                                                  "show_srtp": show_srtp_projects,
                                                  "show_volunteer_activities": show_volunteer_activities,
                                                  "show_practice_projects": show_practice_projects,
                                                  "show_borrowing_rank": show_borrowing_rank,
                                                  "borrowing_rank_percent": borrowing_rank_percent,
                                                  "max_total_borrowed_books_num": max_total_borrowed_books_num,
                                                  "top_borrower_in_unit": top_borrower_in_unit,
                                                  "show_borrowing_detail": show_borrowing_detail,
                                                  "show_gym_ordering_rank": show_gym_ordering_rank,
                                                  "gym_ordering_rank_percent": gym_ordering_rank_percent,
                                                  "days_in_seu": days_in_seu})
