from django.shortcuts import render


def not_eligible_view(request):
    """非本届毕业生提示页面"""
    return render(request, "not_eligible_view.html")
