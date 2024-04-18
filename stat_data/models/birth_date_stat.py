from django.db import models


class BirthDateStat(models.Model):
    """毕业生出生日期统计表"""
    # 出生日期（月日，例如：0501）
    birth_date = models.CharField(max_length=5, primary_key=True, unique=True, verbose_name="出生日期（月日）")
    # 此出生日期的毕业生人数
    count = models.IntegerField(verbose_name="此出生日期的毕业生人数")

    class Meta:
        db_table = "gbd_birth_date_stat"
        verbose_name = "毕业生出生日期统计表"
        verbose_name_plural = verbose_name
        ordering = ["birth_date"]
