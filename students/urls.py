

from django.contrib import admin
from django.urls import path, include
from students import views

urlpatterns = [
    path("", views.student_info),
]
