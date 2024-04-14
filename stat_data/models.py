from django.db import models


class GraduatePersonalStat(models.Model):
    """毕业生个人统计信息表, 用于数据检索、展示"""
    # ---------- 基本 ---------- #
    # 一卡通号
    seu_card_id = models.CharField(max_length=20, primary_key=True, verbose_name="一卡通号", unique=True)
    # 学号
    student_id = models.CharField(max_length=20, verbose_name="学号", null=True, blank=True)
    # 姓名
    full_name = models.CharField(max_length=20, verbose_name="姓名", null=True, blank=True)
    # 学院
    unit_name = models.CharField(max_length=20, verbose_name="学院", null=True, blank=True)
    # 专业
    major = models.CharField(max_length=20, verbose_name="专业", null=True, blank=True)
    # 宿舍名称
    dormitory_name = models.CharField(max_length=20, verbose_name="宿舍名称", null=True, blank=True)
    # 入学时间
    enroll_date = models.DateField(verbose_name="入学时间", null=True, blank=True)

    # ---------- 网络 ---------- #
    # 网络在线天数
    network_online_days = models.CharField(max_length=10, verbose_name="网络在线天数", null=True, blank=True)
    # 网络总流量（GB）
    network_flow = models.CharField(max_length=20, verbose_name="网络总流量(GB)", null=True, blank=True)
    # 流量相当于看了多少甄嬛传（按 167GB 计算）
    # network_flow_equivalence = models.FloatField(verbose_name="流量相当于看了多少甄嬛传", null=True, blank=True)

    # ---------- 食堂 ---------- #
    # 消费次数
    consumption_times = models.CharField(max_length=10, verbose_name="消费次数", null=True, blank=True)
    # 消费金额
    consumption_amount = models.CharField(max_length=10, verbose_name="消费金额", null=True, blank=True)
    # 最频繁消费地点
    most_frequent_consumption_place = models.CharField(max_length=20, verbose_name="最频繁消费地点", null=True,
                                                       blank=True)
    # 最高单次消费
    highest_single_consumption_amount = models.CharField(max_length=10, verbose_name="最高单次消费", null=True,
                                                         blank=True)
    # 最高单次消费日期
    highest_single_consumption_date = models.DateField(verbose_name="最高单次消费日期", null=True, blank=True)

    # ---------- 课程 ---------- #
    # 第一节课日期
    first_class_date = models.DateField(verbose_name="第一节课日期", null=True, blank=True)
    # 第一节课地点
    first_class_place = models.CharField(max_length=20, verbose_name="第一节课地点", null=True, blank=True)
    # 第一节课名称
    first_class_name = models.CharField(max_length=20, verbose_name="第一节课名称", null=True, blank=True)
    # 第一节课教师姓名
    first_class_teacher = models.CharField(max_length=20, verbose_name="第一节课教师姓名", null=True, blank=True)
    # 选课门数
    course_selected_num = models.CharField(max_length=5, verbose_name="选课门数", null=True, blank=True)
    # 获得学分
    credits_obtained = models.CharField(max_length=5, verbose_name="获得学分", null=True, blank=True)
    # 最高分课程名
    highest_score_course = models.CharField(max_length=20, verbose_name="最高分课程名", null=True, blank=True)
    # 论文数量
    papers_num = models.CharField(max_length=5, verbose_name="论文数量", null=True, blank=True)

    # ---------- 人文讲座 ---------- #
    # 参加讲座次数
    lecture_attended_times = models.CharField(max_length=5, verbose_name="参加讲座次数", null=True, blank=True)
    # 第一次参加讲座名称
    first_lecture_name = models.CharField(max_length=100, verbose_name="第一次参加讲座名称", null=True, blank=True)
    # 第一次参加讲座日期
    first_lecture_date = models.DateField(verbose_name="第一次参加讲座日期", null=True, blank=True)

    # ---------- SRTP ---------- #
    # SRTP项目数
    srtp_project_num = models.CharField(max_length=5, verbose_name="SRTP项目数", null=True, blank=True)
    # SRTP学分
    srtp_score = models.CharField(max_length=10, verbose_name="SRTP学分", null=True, blank=True)

    # ---------- 志愿活动 ---------- #
    # 志愿活动数量
    volunteer_activity_num = models.CharField(max_length=5, verbose_name="志愿活动数量", null=True, blank=True)
    # 志愿活动时长
    volunteer_duration = models.CharField(max_length=10, verbose_name="志愿活动时长", null=True, blank=True)

    # ---------- 社会实践 ---------- #
    # 实践项目数量
    practice_project_num = models.CharField(max_length=5, verbose_name="实践项目数量", null=True, blank=True)
    # 第一个实践项目
    first_practice_project_name = models.CharField(max_length=50, verbose_name="第一个实践项目", null=True, blank=True)
    # 第一个实践项目队员（非本人的另一人姓名）
    first_practice_project_member = models.CharField(max_length=20,
                                                     verbose_name="第一个实践项目队员（非本人的另一人姓名）", null=True,
                                                     blank=True)

    # ---------- 图书馆 ---------- #
    # 总借阅量
    total_borrowed_books_num = models.CharField(max_length=10, verbose_name="总借阅量", null=True, blank=True)
    # 最长借阅天数
    longest_book_borrowing_days = models.CharField(max_length=5, verbose_name="最长借阅天数", null=True, blank=True)
    # 个人借阅书籍中总借阅次数最少书名
    nice_book_name = models.CharField(max_length=50, verbose_name="个人借阅书籍中总借阅次数最少书名", null=True,
                                      blank=True)

    # ---------- 体育 ---------- #
    # 场馆预约次数
    gym_ordered_times = models.CharField(max_length=5, verbose_name="场馆预约次数", null=True, blank=True)
    # 首次预约场馆
    first_ordered_gym = models.CharField(max_length=20, verbose_name="首次预约场馆", null=True, blank=True)
    # 首次预约日期
    first_ordered_date = models.DateField(verbose_name="首次预约日期", null=True, blank=True)
    # 跑操次数
    morning_exercise_times = models.CharField(max_length=5, verbose_name="跑操次数", null=True, blank=True)
    # 最早跑操打卡时间
    earliest_exercise_time = models.TimeField(verbose_name="最早跑操打卡时间", null=True, blank=True)

    def __str__(self):
        return f"{self.full_name}[{self.seu_card_id}]"

    class Meta:
        db_table = "graduate_personal_stat"
        verbose_name = "毕业生个人统计信息表"
        verbose_name_plural = verbose_name
        ordering = ["seu_card_id"]
