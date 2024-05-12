from django.db import models


class FavoriteCanteenStat(models.Model):
    """毕业生最常去的食堂统计表"""

    class Meta:
        db_table = "gbd_favorite_canteen_stat"
        verbose_name = "毕业生最常去的食堂统计表"
        verbose_name_plural = verbose_name
        ordering = ["canteen_name"]

    # 食堂名称
    canteen_name = models.CharField(max_length=255, primary_key=True, unique=True, db_comment="食堂名称")
    # 最常去此食堂的毕业生人数
    count = models.IntegerField(db_comment="最常去此食堂的毕业生人数")