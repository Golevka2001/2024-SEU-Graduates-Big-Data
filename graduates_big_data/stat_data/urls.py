from django.urls import path

from . import views

app_name = "stat_data"
urlpatterns = [
    path("", views.index, name="index"),
    path("personal_view", views.personal_view, name="personal_view"),
]
