from django.shortcuts import redirect, render

from django_cas_ng.views import LoginView
from app_main.models import GraduatePersonalStat


def welcome_view(request):
    # 若用户未通过 CAS 认证，则跳转至 CAS 登录页面
    if not request.user.is_authenticated or not request.user.username:
        return LoginView.as_view()(request)

    # 检查是否为本届毕业生，若不在毕业生数据中，则跳转到错误页面，显示仅对本届毕业生开放的提示
    seu_card_id = request.user.username
    if not GraduatePersonalStat.objects.filter(seu_card_id=seu_card_id).exists():
        return redirect("error:not_eligible_view")

    return render(request, "welcome_view.html")
