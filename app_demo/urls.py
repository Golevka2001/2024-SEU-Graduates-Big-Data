from django.urls import path

from . import views

app_name = "app_demo"
urlpatterns = [
    path("", views.welcome_view, name="welcome_view"),
    path("personal_view", views.personal_view, name="personal_view"),
]
