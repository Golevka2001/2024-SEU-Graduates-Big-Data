from django.shortcuts import render


def health_check_view(request):
    """用于健康检查的视图"""
    return render(request, "health_check.html")
