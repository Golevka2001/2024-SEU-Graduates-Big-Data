from django.shortcuts import render


def stat_data_view(request):
    return render(request, "stat_data.html")
