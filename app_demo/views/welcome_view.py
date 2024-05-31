from django.shortcuts import render


def welcome_view(request):
    return render(
        request,
        "demo_welcome_view.html",
    )
