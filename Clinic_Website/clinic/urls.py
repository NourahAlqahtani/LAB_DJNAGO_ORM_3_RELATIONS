from django.urls import path
from . import views

app_name = "clinic"

urlpatterns = [
    path("home/", views.home, name="home")
]