from django.urls import path

from . import views

app_name = "error"
urlpatterns = [
    path("not_eligible/", views.not_eligible_view, name="not_eligible_view"),
]
