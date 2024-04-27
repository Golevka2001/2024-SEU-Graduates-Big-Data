import datetime

from django.conf import settings
from django.shortcuts import render

from stat_data.constants import GRADUATE_TOTAL_NUM

# from django_cas_ng.decorators import login_required
from stat_data.models import FavoriteCanteenStat, GraduatePersonalStat, LibraryBorrowingStat, SportsCompetitionStat

# 只有借阅量排名在前 50% 的毕业生才会显示借阅量排名
SHOW_BORROWING_RANK_THRESHOLD = 0.5


# @login_required  # TODO: 生产环境中启用
def personal_view(request):
    # 获取当前用户的一卡通号
    if settings.ENABLE_CAS:
        seu_card_id = request.user.username
        # TODO: 测试用，后续删除
        if seu_card_id == "TEST_USER":
            seu_card_id = "213216666"
    else:
        seu_card_id = "213216666"
    # 若不在毕业生数据中，则显示提示信息
    if not GraduatePersonalStat.objects.filter(seu_card_id=seu_card_id).exists():
        return render(request, "index.html", {"is_graduate": False})

    # 查询指定毕业生的个人统计信息
    graduate = GraduatePersonalStat.objects.get(seu_card_id=seu_card_id)

    # 流量相当于看了多少甄嬛传（按 167GB 计算）
    network_flow_equivalence = round(float(graduate.network_flow) / 167, 2)

    # 最常去相同食堂的人数
    same_favorite_canteen_cnt = FavoriteCanteenStat.objects.get(
        canteen_name=graduate.most_frequent_consumption_place).count
    same_favorite_canteen_percent = f'{same_favorite_canteen_cnt / GRADUATE_TOTAL_NUM:.2%}'

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
    show_borrowing_rank = borrowing_rank < GRADUATE_TOTAL_NUM * SHOW_BORROWING_RANK_THRESHOLD
    borrowing_rank_percent = f'{1 - borrowing_rank / GRADUATE_TOTAL_NUM:.2%}'

    # 全校最高借阅量（可以写成常量）
    # max_total_borrowed_books_num = LibraryBorrowingStat.objects.order_by("-total_borrowed_books_num")[0]
    max_total_borrowed_books_num = 123

    # 本学院借阅量第一名
    unit_name = graduate.unit_name
    top_borrower_in_unit = \
        LibraryBorrowingStat.objects.filter(unit_name=unit_name).order_by("-total_borrowed_books_num")[0]

    # 是否显示借阅详情
    show_borrowing_detail = int(graduate.total_borrowed_books_num) > 0

    # 是否显示场馆预约
    show_gyms = bool(graduate.first_ordered_gym)

    # 场馆预约次数排名（gym_ordered_times）
    gym_ordering_rank = GraduatePersonalStat.objects.filter(
        gym_ordered_times__gt=graduate.gym_ordered_times).count()
    gym_ordering_rank_percent = f'{1 - gym_ordering_rank / GRADUATE_TOTAL_NUM:.2%}'

    # 是否显示跑操
    show_morning_exercise = int(graduate.morning_exercise_times) > 0

    # 是否显示体育竞赛
    sports_competition_list = SportsCompetitionStat.objects.filter(seu_card_id=seu_card_id)
    show_sports_competitions = bool(sports_competition_list)
    sports_competition = sports_competition_list[0] if show_sports_competitions else None

    # 在学校的第多少天
    days_in_seu = (datetime.date.today() - graduate.enroll_date).days

    return render(request, "personal_view.html", {"graduate": graduate,
                                                  "network_flow_equivalence": network_flow_equivalence,
                                                  "same_favorite_canteen_percent": same_favorite_canteen_percent,
                                                  "show_lecture": show_lectures,
                                                  "show_srtp": show_srtp_projects,
                                                  "show_volunteer_activities": show_volunteer_activities,
                                                  "show_practice_projects": show_practice_projects,
                                                  "show_borrowing_rank": show_borrowing_rank,
                                                  "borrowing_rank_percent": borrowing_rank_percent,
                                                  "max_total_borrowed_books_num": max_total_borrowed_books_num,
                                                  "top_borrower_in_unit": top_borrower_in_unit,
                                                  "show_borrowing_detail": show_borrowing_detail,
                                                  "show_gyms": show_gyms,
                                                  "gym_ordering_rank_percent": gym_ordering_rank_percent,
                                                  "show_morning_exercise": show_morning_exercise,
                                                  "show_sports_competitions": show_sports_competitions,
                                                  "sports_competition": sports_competition,
                                                  "days_in_seu": days_in_seu})
