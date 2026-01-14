from django.contrib import admin
from django.urls import path, include
from students import views

urlpatterns = [
    path("list/", views.StudnetListModelMixin.as_view(), name="list"),
    path("", views.student_info),
    path("<int:pk>", views.student_info),
    path("payments/", views.StudentPaymentCreate.as_view()),
    path("payments/<int:pk>", views.StudentPaymentCreate.as_view()),
]
