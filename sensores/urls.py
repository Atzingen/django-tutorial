from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("sensor_input/<int:valor>", views.sensor_input, name="sensor_input"),
]