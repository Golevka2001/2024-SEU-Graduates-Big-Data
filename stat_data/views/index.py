from django.shortcuts import render

from django_cas_ng.views import LoginView
from stat_data.models import GraduatePersonalStat


def index(request):
    # 若用户已通过 CAS 认证
    if request.user.is_authenticated:
        # 检查是否为本届毕业生
        seu_card_id = request.user.username
        # TODO: 测试用，后续删除
        if seu_card_id == "TEST_USER":
            seu_card_id = "213216666"
        if GraduatePersonalStat.objects.filter(seu_card_id=seu_card_id).exists():
            return render(request, "index.html", {"is_graduate": True})

        # 若不在毕业生数据中，则显示提示信息
        return render(request, "index.html", {"is_graduate": False})

    # 若用户未通过 CAS 认证，则跳转至 CAS 登录页面
    return LoginView.as_view()(request)
