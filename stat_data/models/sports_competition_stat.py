from django.db import models


class SportsCompetitionStat(models.Model):
    """体育赛事统计表"""
    # 一卡通号
    seu_card_id = models.CharField(max_length=20, primary_key=True, verbose_name="一卡通号", unique=True)
    # 学号
    student_id = models.CharField(max_length=20, verbose_name="学号")
    # 姓名
    full_name = models.CharField(max_length=20, verbose_name="姓名")
    # 学院
    unit_name = models.CharField(max_length=20, primary_key=True, verbose_name="学院")
    # 竞赛类型
    competition_type = models.CharField(max_length=5, verbose_name="竞赛类型")
    # 竞赛名称
    competition_name = models.CharField(max_length=50, verbose_name="竞赛名称")
    # 项目
    sports_events = models.CharField(max_length=20, verbose_name="项目")
    # 成绩
    score = models.CharField(max_length=20, verbose_name="成绩")
    # 排名
    rank = models.CharField(max_length=20, verbose_name="排名")

    class Meta:
        db_table = "gbd_sports_competition_stat"
        verbose_name = "体育赛事统计表"
        verbose_name_plural = verbose_name
        ordering = ["seu_card_id"]
