from django.db import models


class GraduatePersonalStat(models.Model):
    """毕业生个人统计信息表, 用于数据检索、展示"""
    # ---------- 枚举 ---------- #
    # 毕业生类型: 0-本科毕业生; 1-硕士毕业生; 2-博士毕业生
    GRADUATE_TYPE_CHOICES = [
        (0, "本科毕业生"),
        (1, "硕士毕业生"),
        (2, "博士毕业生"),
    ]

    # ---------- 基本 ---------- #
    # 一卡通号
    seu_card_id = models.CharField(max_length=20, primary_key=True, verbose_name="一卡通号", unique=True)
    # 学号
    student_id = models.CharField(max_length=20, verbose_name="学号")
    # 姓名
    full_name = models.CharField(max_length=255, verbose_name="姓名")
    # 学院
    unit_name = models.CharField(max_length=255, verbose_name="学院")
    # 专业
    major = models.CharField(max_length=255, verbose_name="专业")
    # 【存在空】宿舍名称
    dormitory_name = models.CharField(max_length=255, verbose_name="宿舍名称", null=True)
    # 入学时间
    enroll_date = models.DateField(verbose_name="入学时间")
    # 毕业生类型: 0-本科毕业生; 1-硕士毕业生; 2-博士毕业生
    graduate_type = models.IntegerField(choices=GRADUATE_TYPE_CHOICES, verbose_name="毕业生类型")
    # 【存在空】生源地
    origin = models.CharField(max_length=255, verbose_name="生源地", null=True)
    # 【存在空】相同生源地人数
    same_origin_num = models.CharField(max_length=100, verbose_name="相同生源地人数", null=True, default="0")
    # 【存在空】相同生日人数
    same_birthdate_num = models.CharField(max_length=100, verbose_name="相同生日人数", null=True, default="0")

    # ---------- 网络 ---------- #
    # 【存在空】网络在线天数
    network_online_days = models.CharField(max_length=255, verbose_name="网络在线天数", null=True, default="0")
    # 【存在空】网络总流量（GB）
    network_flow = models.CharField(max_length=255, verbose_name="网络总流量(GB)", null=True, default="0.00")

    # ---------- 食堂 ---------- #
    # 【存在空】消费次数
    consumption_times = models.CharField(max_length=255, verbose_name="消费次数", null=True, default="0")
    # 【存在空】消费金额
    consumption_amount = models.CharField(max_length=255, verbose_name="消费金额", null=True, default="0.00")
    # 最频繁消费地点
    most_frequent_consumption_place = models.CharField(max_length=255, verbose_name="最频繁消费地点", null=True)
    # 【存在空】最高单次消费
    highest_single_consumption_amount = models.CharField(max_length=255, verbose_name="最高单次消费", null=True,
                                                         default="0.00")
    # 【存在空】最高单次消费日期
    highest_single_consumption_date = models.DateField(verbose_name="最高单次消费日期", null=True)

    # ---------- 课程 ---------- #
    # 【存在空】第一节课日期
    first_class_date = models.DateField(verbose_name="第一节课日期", null=True)
    # 【存在空】第一节课地点
    first_class_place = models.CharField(max_length=255, verbose_name="第一节课地点", null=True)
    # 【存在空】第一节课名称
    first_class_name = models.CharField(max_length=255, verbose_name="第一节课名称", null=True)
    # 【存在空】第一节课教师姓名
    first_class_teacher = models.CharField(max_length=255, verbose_name="第一节课教师姓名", null=True)
    # 【存在空】选课门数
    course_selected_num = models.CharField(max_length=255, verbose_name="选课门数", null=True, default="0")
    # 【存在空】获得学分
    credits_obtained = models.CharField(max_length=255, verbose_name="获得学分", null=True, default="0.00")
    # 【存在空】最高分课程名
    highest_score_course = models.CharField(max_length=255, verbose_name="最高分课程名", null=True)
    # 【存在空】论文数量
    papers_num = models.CharField(max_length=255, verbose_name="论文数量", null=True, default="0")

    # ---------- 人文讲座 ---------- #
    # 【存在空】参加讲座次数
    lecture_attended_times = models.CharField(max_length=255, verbose_name="参加讲座次数", null=True, default="0")
    # 【存在空】第一次参加讲座名称
    first_lecture_name = models.CharField(max_length=255, verbose_name="第一次参加讲座名称", null=True)
    # 【存在空】第一次参加讲座日期
    first_lecture_date = models.DateField(verbose_name="第一次参加讲座日期", null=True)

    # ---------- SRTP ---------- #
    # 【存在空】SRTP项目数
    srtp_project_num = models.CharField(max_length=255, verbose_name="SRTP项目数", null=True, default="0")
    # 【存在空】SRTP学分
    srtp_score = models.CharField(max_length=255, verbose_name="SRTP学分", null=True, default="0.00")

    # ---------- 志愿活动 ---------- #
    # 志愿活动数量
    volunteer_activity_num = models.CharField(max_length=255, verbose_name="志愿活动数量", null=True, default="0")
    # 【存在空】志愿活动时长
    volunteer_duration = models.CharField(max_length=255, verbose_name="志愿活动时长", null=True, default="0.00")

    # ---------- 社会实践 ---------- #
    # 【存在空】实践项目数量
    practice_project_num = models.CharField(max_length=255, verbose_name="实践项目数量", null=True, default="0")
    # 【存在空】第一个实践项目
    first_practice_project_name = models.CharField(max_length=255, verbose_name="第一个实践项目", null=True)
    # 【存在空】第一个实践项目队员（非本人的另一人姓名）
    first_practice_project_member = models.CharField(max_length=255,
                                                     verbose_name="第一个实践项目队员（非本人的另一人姓名）", null=True)

    # ---------- 图书馆 ---------- #
    # 【存在空】总借阅量
    total_borrowed_books_num = models.CharField(max_length=255, verbose_name="总借阅量", null=True, default="0")
    # 【存在空】最长借阅天数
    longest_book_borrowing_days = models.CharField(max_length=255, verbose_name="最长借阅天数", null=True, default="0")
    # 【存在空】个人借阅书籍中总借阅次数最少书名
    nice_book_name = models.CharField(max_length=255, verbose_name="个人借阅书籍中总借阅次数最少书名", null=True)
    # 【存在空】个人借阅书籍中总借阅次数最少的书被多少人借过
    nice_book_borrowing_person_num = models.CharField(max_length=255,
                                                      verbose_name="个人借阅书籍中总借阅次数最少的书被多少人借过",
                                                      null=True)
    # 【存在空】借阅时间最长的书名
    longest_keeping_book_name = models.CharField(max_length=255, verbose_name="借阅时间最长的书名", null=True)

    # ---------- 体育 ---------- #
    # 【存在空】场馆预约次数
    gym_ordered_times = models.CharField(max_length=255, verbose_name="场馆预约次数", null=True, default="0")
    # 【存在空】首次预约场馆
    first_ordered_gym = models.CharField(max_length=255, verbose_name="首次预约场馆", null=True)
    # 【存在空】首次预约日期
    first_ordered_date = models.DateField(verbose_name="首次预约日期", null=True)
    # 【存在空】最常去的场馆
    favorite_gym = models.CharField(max_length=255, verbose_name="最常去的场馆", null=True)
    # 【存在空】最常去的场馆预约次数
    favorite_gym_ordered_times = models.CharField(max_length=255, verbose_name="最常去的场馆预约次数", null=True,
                                                  default="0")
    # 【存在空】跑操次数
    morning_exercise_times = models.CharField(max_length=255, verbose_name="跑操次数", null=True, default="0")
    # 【存在空】最早跑操打卡时间
    earliest_exercise_time = models.TimeField(verbose_name="最早跑操打卡时间", null=True)

    def __str__(self):
        return f"{self.full_name}[{self.seu_card_id}]"

    class Meta:
        db_table = "gbd_graduate_personal_stat"
        verbose_name = "毕业生个人统计信息表"
        verbose_name_plural = verbose_name
        ordering = ["seu_card_id"]
