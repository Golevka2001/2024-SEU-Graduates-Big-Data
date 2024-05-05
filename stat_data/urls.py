from django.urls import path

from . import views

app_name = "stat_data"
urlpatterns = [
    path("", views.welcome_view, name="welcome_view"),
    path("personal_view", views.personal_view, name="personal_view"),
    path("test", views.test, name="test"),
]
