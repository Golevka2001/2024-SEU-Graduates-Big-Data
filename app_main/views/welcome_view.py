from django.shortcuts import render

from app_main.models import GraduatePersonalStat
from django_cas_ng.views import LoginView


def welcome_view(request):
    # 若用户未通过 CAS 认证，则跳转至 CAS 登录页面
    if not request.user.is_authenticated or not request.user.username:
        return LoginView.as_view()(request)

    # 检查是否为本届毕业生，若不在毕业生数据中，则跳转到错误页面，显示仅对本届毕业生开放的提示
    seu_card_id = request.user.username
    is_eligible = True
    graduate_name = None
    if (
        not GraduatePersonalStat.objects.only("seu_card_id")
        .filter(seu_card_id=seu_card_id)
        .exists()
    ):
        is_eligible = False
    else:
        graduate_name = (
            GraduatePersonalStat.objects.only("seu_card_id", "full_name")
            .get(seu_card_id=seu_card_id)
            .full_name
        )

    # 内测用户检查
    with open("./test_users.txt", "r") as f:
        test_users = f.read().splitlines()
    if seu_card_id not in test_users:
        is_eligible = False

    return render(
        request,
        "welcome_view.html",
        {
            "is_eligible": is_eligible,
            "graduate_name": graduate_name,
        },
    )
