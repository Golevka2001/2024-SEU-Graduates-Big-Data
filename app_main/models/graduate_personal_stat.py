from datetime import date

from django.db import models


class GraduatePersonalStat(models.Model):
    """毕业生个人统计信息表, 用于数据检索、展示"""

    class Meta:
        db_table = "gbd_graduate_personal_stat"
        verbose_name = "毕业生个人统计信息表"
        verbose_name_plural = verbose_name
        ordering = ["seu_card_id"]

    # ---------- 枚举 ---------- #
    # 毕业生类型: 0-本科毕业生; 1-硕士毕业生; 2-博士毕业生
    GRADUATE_TYPE_CHOICES = [
        (0, "本科毕业生"),
        (1, "硕士毕业生"),
        (2, "博士毕业生"),
    ]

    # ---------- 基本 ---------- #
    # 一卡通号
    seu_card_id = models.CharField(
        max_length=255, primary_key=True, db_comment="一卡通号", unique=True
    )
    # 姓名
    full_name = models.CharField(max_length=255, db_comment="姓名")
    # 毕业生类型: 0-本科毕业生; 1-硕士毕业生; 2-博士毕业生
    graduate_type = models.IntegerField(
        choices=GRADUATE_TYPE_CHOICES, db_comment="毕业生类型"
    )

    # ---------- 场景1: 大门 ---------- #
    # 入学时间
    enroll_date = models.DateField(db_comment="入学时间")
    # 生源地
    origin = models.CharField(max_length=255, db_comment="生源地", null=True)
    # 相同生日人数
    same_birthdate_num = models.CharField(
        max_length=255, db_comment="相同生日人数", null=True, default="0"
    )
    # 相同生源地人数
    same_origin_num = models.CharField(
        max_length=255, db_comment="相同生源地人数", null=True, default="0"
    )

    # ---------- 场景2: 宿舍 ---------- #
    # 宿舍名称
    dormitory_name = models.CharField(max_length=255, db_comment="宿舍名称", null=True)
    # 网络在线天数
    network_online_days = models.CharField(
        max_length=255, db_comment="网络在线天数", null=True, default="0"
    )
    # 网络总流量（TB）
    network_flow = models.CharField(
        max_length=255, db_comment="网络总流量(TB)", null=True, default="0.00"
    )

    # ---------- 场景3: 食堂 ---------- #
    # 消费金额
    consumption_amount = models.CharField(
        max_length=255, db_comment="消费金额", null=True, default="0.00"
    )
    # 消费次数
    consumption_times = models.CharField(
        max_length=255, db_comment="消费次数", null=True, default="0"
    )
    # 最频繁消费地点
    most_frequent_consumption_place = models.CharField(
        max_length=255, db_comment="最频繁消费地点", null=True
    )
    # 最高单次消费日期
    highest_single_consumption_date = models.DateField(
        db_comment="最高单次消费日期", null=True
    )
    # 最高单次消费
    highest_single_consumption_amount = models.CharField(
        max_length=255, db_comment="最高单次消费", null=True, default="0.00"
    )

    # ---------- 场景4: 教室 ---------- #
    # 学院
    unit_name = models.CharField(max_length=255, db_comment="学院")
    # 专业
    major = models.CharField(max_length=255, db_comment="专业")
    # 第一节课日期
    first_class_date = models.DateField(db_comment="第一节课日期", null=True)
    # 第一节课地点
    first_class_place = models.CharField(
        max_length=255, db_comment="第一节课地点", null=True
    )
    # 第一节课教师姓名
    first_class_teacher = models.CharField(
        max_length=255, db_comment="第一节课教师姓名", null=True
    )
    # 第一节课名称
    first_class_name = models.CharField(
        max_length=255, db_comment="第一节课名称", null=True
    )
    # 选课门数
    course_selected_num = models.CharField(
        max_length=255, db_comment="选课门数", null=True, default="0"
    )
    # 获得学分
    credits_obtained = models.CharField(
        max_length=255, db_comment="获得学分", null=True, default="0.00"
    )
    # 最高分课程名
    highest_score_course = models.CharField(
        max_length=255, db_comment="最高分课程名", null=True
    )

    # ---------- 场景5: 报告厅 ---------- #
    # 参加讲座次数
    lecture_attended_times = models.CharField(
        max_length=255, db_comment="参加讲座次数", null=True, default="0"
    )
    # 第一次参加讲座时间
    first_lecture_date = models.DateField(db_comment="第一次参加讲座时间", null=True)
    # 第一次参加讲座名称
    first_lecture_name = models.CharField(
        max_length=255, db_comment="第一次参加讲座名称", null=True
    )
    # SRTP项目数
    srtp_project_num = models.CharField(
        max_length=255, db_comment="SRTP项目数", null=True, default="0"
    )
    # SRTP学分
    srtp_score = models.CharField(
        max_length=255, db_comment="SRTP学分", null=True, default="0.00"
    )
    # 志愿活动数量
    volunteer_activity_num = models.CharField(
        max_length=255, db_comment="志愿活动数量", null=True, default="0"
    )
    # 志愿活动时长
    volunteer_duration = models.CharField(
        max_length=255, db_comment="志愿活动时长", null=True, default="0.00"
    )
    # 社会实践项目数量
    practice_project_num = models.CharField(
        max_length=255, db_comment="社会实践项目数量", null=True, default="0"
    )
    # 第一个社会实践项目队员（非本人的另一人姓名）
    first_practice_project_member = models.CharField(
        max_length=255,
        db_comment="第一个社会实践项目队员（非本人的另一人姓名）",
        null=True,
    )
    # 第一个社会实践项目名称
    first_practice_project_name = models.CharField(
        max_length=255, db_comment="第一个社会实践项目名称", null=True
    )

    # ---------- 场景6: 图书馆 ---------- #
    # 总借阅量
    total_borrowed_books_num = models.CharField(
        max_length=255, db_comment="总借阅量", null=True, default="0"
    )
    # 借阅时间最长的书名
    longest_keeping_book_name = models.CharField(
        max_length=255, db_comment="借阅时间最长的书名", null=True
    )
    # 最长借阅天数
    longest_book_borrowing_days = models.CharField(
        max_length=255, db_comment="最长借阅天数", null=True, default="0 days 00:00:00"
    )
    # 个人借阅书籍中总借阅次数最少书名
    nice_book_name = models.CharField(
        max_length=255, db_comment="个人借阅书籍中总借阅次数最少书名", null=True
    )
    # 个人借阅书籍中总借阅次数最少的书被多少人借过
    nice_book_borrowing_person_num = models.CharField(
        max_length=255,
        db_comment="个人借阅书籍中总借阅次数最少的书被多少人借过",
        null=True,
    )
    # 进出图书馆次数
    library_visits = models.CharField(
        max_length=255, db_comment="进出图书馆次数", null=True, default="0"
    )

    # ---------- 场景7: 体育馆 ---------- #
    # 首次预约日期
    first_ordered_date = models.DateField(db_comment="首次预约日期", null=True)
    # 首次预约场馆
    first_ordered_gym = models.CharField(
        max_length=255, db_comment="首次预约场馆", null=True
    )
    # 场馆预约次数
    gym_ordered_times = models.CharField(
        max_length=255, db_comment="场馆预约次数", null=True, default="0"
    )
    # 最常去的场馆
    favorite_gym = models.CharField(
        max_length=255, db_comment="最常去的场馆", null=True
    )
    # 最常去的场馆预约次数
    favorite_gym_ordered_times = models.CharField(
        max_length=255, db_comment="最常去的场馆预约次数", null=True, default="0"
    )
    # 跑操次数
    morning_exercise_times = models.CharField(
        max_length=255, db_comment="跑操次数", null=True, default="0"
    )
    # 最早跑操打卡时间
    earliest_exercise_time = models.DateField(db_comment="最早跑操打卡时间", null=True)

    # ----- 判断是否显示某部分文案的函数 ----- #
    def is_birthdate_unique(self):
        return int(self.same_birthdate_num or 0) <= 0

    def show_same_origin_num(self):
        return int(self.same_origin_num or 0) > 0

    def show_network_data(self):
        return (
            int(self.network_online_days or 0) > 0
            and float(self.network_flow or 0.0) > 0.0
        )

    def show_first_class_data(self):
        return (
            bool(self.first_class_date)
            and bool(self.first_class_teacher)
            and bool(self.first_class_name)
        )

    def show_lectures(self):
        return (
            int(self.lecture_attended_times or 0) > 0
            and bool(self.first_lecture_date)
            and bool(self.first_lecture_name)
        )

    def show_srtp_projects(self):
        return (
            int(self.srtp_project_num or 0) > 0 and float(self.srtp_score or 0.0) > 0.0
        )

    def show_volunteer_activities(self):
        return (
            int(self.volunteer_activity_num or 0) > 0
            and float(self.volunteer_duration or 0.0) > 0.0
        )

    def show_practice_projects(self):
        return (
            int(self.practice_project_num or 0) > 0
            and bool(self.first_practice_project_member)
            and bool(self.first_practice_project_name)
        )

    def show_additional_content_in_auditorium_page(self):
        cnt = 0
        cnt += self.show_lectures()
        cnt += self.show_srtp_projects()
        cnt += self.show_volunteer_activities()
        cnt += self.show_practice_projects()
        return cnt <= 1

    def lack_of_borrowing_data(self):
        return (
            int(self.total_borrowed_books_num or 0) <= 0
            or int(self.get_longest_book_borrowing_days()) <= 0
            or not bool(self.nice_book_name)
        )

    def show_gym_data(self):
        return bool(self.first_ordered_date) and bool(self.first_ordered_gym)

    def show_gym_details(self):
        return (
            int(self.gym_ordered_times or 0) >= 10
            and bool(self.favorite_gym)
            and int(self.favorite_gym_ordered_times or 0) > 0
        )

    def show_morning_exercise(self):
        return int(self.morning_exercise_times or 0) > 0

    # ----- 判断是否跳过某整个页面的函数 ----- #
    def show_dormitory_page(self):
        return bool(self.dormitory_name) or self.show_network_data()

    def show_canteen_page(self):
        return bool(self.most_frequent_consumption_place) or bool(
            self.highest_single_consumption_date
        )

    def show_auditorium_page(self):
        return (
            bool(self.first_lecture_date)
            or self.show_srtp_projects()
            or self.show_volunteer_activities()
            or bool(self.first_practice_project_name)
        )

    def show_library_page(self):
        return not self.lack_of_borrowing_data() or int(self.library_visits or 0) >= 10

    def show_gym_page(self):
        return bool(self.favorite_gym) or bool(self.earliest_exercise_time)

    # ----- 用于计算的函数 ----- #
    def get_network_flow_equivalence(self):
        return round(float(self.network_flow or 0.0) * 1024 / 70, 2)

    def get_longest_book_borrowing_days(self):
        # 存储格式为：(xx days) xx:xx:xx
        if not self.longest_book_borrowing_days:
            return "0"
        if "days" not in self.longest_book_borrowing_days:
            return "0"
        return self.longest_book_borrowing_days.split(" ")[0]

    def get_days_in_seu(self):
        return (date.today() - self.enroll_date).days
