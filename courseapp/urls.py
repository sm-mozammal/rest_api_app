from django.urls import path
from courseapp import views


urlpatterns = [
    path("", views.CourseListView.as_view()),
    path("<int:pk>", views.CourseListModify.as_view()),
    path("create", views.CourseListCreate.as_view()),
    path("create/<int:pk>", views.Course_Retrive_Update_Destroy.as_view()),
]
