from django.urls import path

from . import views

urlpatterns = [
    path("", views.stat_data_view, name="stat_data"),
]
