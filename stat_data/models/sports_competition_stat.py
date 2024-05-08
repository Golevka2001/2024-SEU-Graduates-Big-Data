from django.db import models


class SportsCompetitionStat(models.Model):
    """体育赛事统计表"""

    class Meta:
        db_table = "gbd_sports_competition_stat"
        verbose_name = "体育赛事统计表"
        verbose_name_plural = verbose_name
        ordering = ["seu_card_id"]

    # 一卡通号
    seu_card_id = models.CharField(max_length=255, db_comment="一卡通号")
    # 学号
    student_id = models.CharField(max_length=255, db_comment="学号", null=True)
    # 姓名
    full_name = models.CharField(max_length=255, db_comment="姓名", null=True)
    # 学院
    unit_name = models.CharField(max_length=255, db_comment="学院", null=True)
    # 竞赛类型
    competition_type = models.CharField(max_length=255, db_comment="竞赛类型")
    # 竞赛名称
    competition_name = models.CharField(max_length=255, db_comment="竞赛名称")
    # 项目
    sports_events = models.CharField(max_length=255, db_comment="项目", null=True)
    # 成绩
    score = models.CharField(max_length=255, db_comment="成绩", null=True)
