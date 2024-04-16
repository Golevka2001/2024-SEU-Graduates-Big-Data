from django.shortcuts import render

from stat_data.models import (GraduatePersonalStat, BirthDateStat, OriginStat,
                              LibraryBorrowingStat)


def stat_data_view(request):
    # 当前所查询毕业生的一卡通号
    seu_card_id = "213216666"  # TODO: 测试用，后续删除
    graduate = GraduatePersonalStat.objects.get(seu_card_id=seu_card_id)

    # 相同出生月日的毕业生人数
    birth_date = graduate.birth_date
    same_birth_date_cnt = BirthDateStat.objects.get(birth_date=birth_date).count - 1

    # 相同生源地的毕业生人数
    origin = graduate.origin
    same_origin_cnt = OriginStat.objects.get(origin=origin).count - 1

    # 流量相当于看了多少甄嬛传（按 167GB 计算）
    network_flow_equivalence = float(graduate.network_flow) / 167

    # 全校最高借阅量（可以写成常量）
    # max_total_borrowed_books_num = LibraryBorrowingStat.objects.order_by("-total_borrowed_books_num")[0]
    max_total_borrowed_books_num = 123

    # 本学院借阅量第一名
    unit_name = graduate.unit_name
    top_borrower_in_unit = LibraryBorrowingStat.objects.filter(unit_name=unit_name).order_by("-borrow_times")[0]

    return render(request, "stat_data.html", {"graduate": graduate,
                                              "same_birth_date_cnt": same_birth_date_cnt,
                                              "same_origin_cnt": same_origin_cnt,
                                              "network_flow_equivalence": network_flow_equivalence,
                                              "max_total_borrowed_books_num": max_total_borrowed_books_num,
                                              "top_borrower_in_unit": top_borrower_in_unit})
