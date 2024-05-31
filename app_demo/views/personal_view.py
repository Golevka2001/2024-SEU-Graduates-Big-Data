from django.shortcuts import render


def personal_view(request):
    return render(
        request,
        "demo_personal_view.html",
    )
