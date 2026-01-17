from django.shortcuts import render
from rest_framework.generics import (
    GenericAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
)
from .models import CourseModel
from .serializers import CourseSerializer
from rest_framework import viewsets


# Crud api with viewsets
class Course_Model_View_Sets(viewsets.ModelViewSet):
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer


# Create your views here.
class CourseListView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer

    def get(self, request, *args, **kwargs):
        todoList = self.get_queryset()
        serializer = self.get_serializer(todoList, many=True)
        print(serializer.data)
        message = (
            "Course fetched successfully" if todoList.exists() else "No Course found"
        )
        return Response(
            {"message": message, "status": status.HTTP_200_OK, "data": serializer.data}
        )
        # return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.create(request, *args, **kwargs)
        return Response(
            {"message": "Successfully Added"},
        )


class CourseListModify(
    GenericAPIView,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
):
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CourseListCreate(ListCreateAPIView):
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer


class Course_Retrive_Update_Destroy(RetrieveUpdateDestroyAPIView):
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer
