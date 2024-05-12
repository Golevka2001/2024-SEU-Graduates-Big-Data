from django.urls import path

from . import views

app_name = "app_health_check"
urlpatterns = [
    path("", views.health_check_view, name="health_check_view"),
]
