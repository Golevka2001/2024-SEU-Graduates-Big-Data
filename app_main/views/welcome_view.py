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
    if not GraduatePersonalStat.objects.filter(seu_card_id=seu_card_id).exists():
        is_eligible = False

    graduate_name = GraduatePersonalStat.objects.get(seu_card_id=seu_card_id).full_name
    return render(
        request,
        "welcome_view.html",
        {
            "is_eligible": is_eligible,
            "graduate_name": graduate_name,
        },
    )
