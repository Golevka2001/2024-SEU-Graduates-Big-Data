from django.db import models


class OrderingRankStat(models.Model):
    """毕业生场馆预约次数排名表"""

    class Meta:
        db_table = "gbd_ordering_rank_stat"
        verbose_name = "毕业生场馆预约次数排名表"
        verbose_name_plural = verbose_name
        ordering = ["ordering_rank"]

    # 场馆预约次数
    ordering_times = models.IntegerField(
        db_comment="场馆预约次数", primary_key=True, unique=True
    )
    # 此预约次数在全体毕业生中的排名
    ordering_rank = models.IntegerField(db_comment="此预约次数在全体毕业生中的排名")
