from django.shortcuts import render


def personal_view(request):
    return render(
        request,
        "personal_view.html",
    )
