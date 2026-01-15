from django.urls import path
from students import views

urlpatterns = [
    path("", views.student_info),
    path("<int:pk>", views.student_info),
    path("payments/", views.StudentPaymentCreate.as_view()),
    path("payments/<int:pk>", views.StudentPaymentCreate.as_view()),
    path("list/", views.StudnetListModelMixin.as_view(), name="list"),
    path("create/", views.StudentCreateModelMixin.as_view()),
    path("list/<int:pk>", views.StudentRetrive.as_view(), name="list"),
    path("update/<int:pk>", views.StudentUpdate.as_view()),
    path("delete/<int:pk>", views.StudentDetele.as_view()),
]
