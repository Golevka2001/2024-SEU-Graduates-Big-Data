from django.shortcuts import render

from stat_data.models import GraduatePersonalStat


def stat_data_view(request):
    seu_card_id = "213216666"  # TODO: 测试用，后续删除
    graduate = GraduatePersonalStat.objects.get(seu_card_id=seu_card_id)
    return render(request, "stat_data.html", {"graduate": graduate})
