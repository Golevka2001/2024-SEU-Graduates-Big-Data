from django.db import models


class OriginStat(models.Model):
    """毕业生生源地统计表"""
    # 生源地
    origin = models.CharField(max_length=50, primary_key=True, unique=True, verbose_name="生源地")
    # 此生源地的毕业生人数
    count = models.IntegerField(verbose_name="此生源地的毕业生人数")

    class Meta:
        db_table = "gbd_origin_stat"
        verbose_name = "毕业生生源地统计表"
        verbose_name_plural = verbose_name
        ordering = ["origin"]
