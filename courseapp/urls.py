from django.urls import path, include
from courseapp import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register("viewsets", views.Course_Model_View_Sets, basename="course")

urlpatterns = [
    path("", views.CourseListView.as_view()),
    path("<int:pk>", views.CourseListModify.as_view()),
    path("create", views.CourseListCreate.as_view()),
    path("create/<int:pk>", views.Course_Retrive_Update_Destroy.as_view()),
    path("", include(router.urls)),
]
