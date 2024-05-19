from django.db import models


class BorrowingRankStat(models.Model):
    """毕业生借阅量排名表"""

    class Meta:
        db_table = "gbd_borrowing_rank_stat"
        verbose_name = "毕业生借阅量排名表"
        verbose_name_plural = verbose_name
        ordering = ["borrowing_rank"]

    # 借阅量
    borrowing_num = models.IntegerField(
        db_comment="借阅量", primary_key=True, unique=True
    )
    # 此借阅量在全体毕业生中的排名
    borrowing_rank = models.IntegerField(db_comment="此借阅量在全体毕业生中的排名")
