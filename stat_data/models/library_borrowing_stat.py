from django.db import models


class LibraryBorrowingStat(models.Model):
    """图书馆借阅数据表"""
    # 学院
    unit_name = models.CharField(max_length=20, primary_key=True, verbose_name="学院")
    # 借阅量在学院中的排名
    rank = models.IntegerField(verbose_name="借阅量在学院中的排名")
    # 一卡通号
    seu_card_id = models.CharField(max_length=20, verbose_name="一卡通号")
    # 姓名
    full_name = models.CharField(max_length=20, verbose_name="姓名")
    # 总借阅量
    total_borrowed_books_num = models.CharField(max_length=10, verbose_name="总借阅量")

    class Meta:
        db_table = "gbd_library_borrowing_stat"
        verbose_name = "图书馆借阅数据表"
        verbose_name_plural = verbose_name
        ordering = ["unit_name", "rank"]
