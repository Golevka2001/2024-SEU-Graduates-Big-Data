from django.db import models


class FavoriteCanteenStat(models.Model):
    """毕业生最常去的食堂统计表"""
    # 食堂名称
    canteen_name = models.CharField(max_length=20, primary_key=True, unique=True, verbose_name="食堂名称")
    # 最常去此食堂的毕业生人数
    count = models.IntegerField(verbose_name="最常去此食堂的毕业生人数")

    class Meta:
        db_table = "gbd_favorite_canteen_stat"
        verbose_name = "毕业生最常去的食堂统计表"
        verbose_name_plural = verbose_name
        ordering = ["canteen_name"]
