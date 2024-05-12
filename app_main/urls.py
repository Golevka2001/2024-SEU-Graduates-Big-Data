from django.urls import path

from . import views

app_name = "app_main"
urlpatterns = [
    path("", views.welcome_view, name="welcome_view"),
    path("personal_view", views.personal_view, name="personal_view"),
    path("test", views.test_view, name="test_view"),
]
