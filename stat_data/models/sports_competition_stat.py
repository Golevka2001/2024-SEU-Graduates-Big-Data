from django.db import models


class SportsCompetitionStat(models.Model):
    """体育赛事统计表"""
    # 一卡通号
    seu_card_id = models.CharField(max_length=255, primary_key=True, verbose_name="一卡通号", unique=True)
    # 学号
    student_id = models.CharField(max_length=255, verbose_name="学号", null=True)
    # 姓名
    full_name = models.CharField(max_length=255, verbose_name="姓名", null=True)
    # 学院
    unit_name = models.CharField(max_length=255, verbose_name="学院", null=True)
    # 竞赛类型
    competition_type = models.CharField(max_length=255, verbose_name="竞赛类型")
    # 竞赛名称
    competition_name = models.CharField(max_length=255, verbose_name="竞赛名称")
    # 项目
    sports_events = models.CharField(max_length=255, verbose_name="项目", null=True)
    # 成绩
    score = models.CharField(max_length=255, verbose_name="成绩")

    class Meta:
        db_table = "gbd_sports_competition_stat"
        verbose_name = "体育赛事统计表"
        verbose_name_plural = verbose_name
        ordering = ["seu_card_id"]
