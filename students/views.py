from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Students, StudentPayment
from .serializers import StudentSerializer, StudentPaymentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)


# Create your views here. (Function Based)
@api_view(["GET", "POST", "PUT", "PATCH", "DELETE"])
def student_info(request, pk=None):
    if request.method == "GET":
        id = pk
        if id is not None:
            student = Students.objects.get(id=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)

        sdata = Students.objects.all()
        serializer = StudentSerializer(sdata, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Successfully Added"})
        return Response(serializer.errors)
    if request.method == "PUT":
        id = pk
        student = Students.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Updated Data Successfully"})
        return Response({"error": serializer.errors})
    if request.method == "PATCH":
        id = pk
        student = Students.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Updated Data Successfully"})
        return Response({"error": serializer.errors})
    if request.method == "DELETE":
        id = pk
        student = Students.objects.get(id=id)
        student.delete()
        return Response({"message": "Deleted Successfully"})


# with class base api view
class StudentPaymentCreate(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            student = StudentPayment.objects.get(id=id)
            serializer = StudentPaymentSerializer(student)
            return Response(serializer.data)

        sdata = StudentPayment.objects.all()
        serializer = StudentPaymentSerializer(sdata, many=True)
        return Response(serializer.data)

    def post(self, request, formate=None):
        serializer = StudentPaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Successfully Added"})
        return Response(serializer.errors)

    def put(self, request, pk, format=None):
        id = pk
        payment = StudentPayment.objects.get(id=id)
        serializer = StudentPaymentSerializer(payment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Updated Data Successfully"})
        return Response({"error": serializer.errors})

    def patch(self, request, pk, formate=None):
        id = pk
        payment = StudentPayment.objects.get(id=id)
        serializer = StudentPaymentSerializer(payment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Updated Data Successfully"})
        return Response({"error": serializer.errors})

    def delete(self, request, pk, formate=None):
        id = pk
        payment = StudentPayment.objects.get(id=id)
        payment.delete()
        return Response({"message": "Deleted Data Successfully"})


# ListModelMixin Get Students data
class StudnetListModelMixin(GenericAPIView, ListModelMixin):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# ListModelMixin Crate Students data
class StudentCreateModelMixin(GenericAPIView, CreateModelMixin):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# ListModelMixin get single Students data
class StudentRetrive(GenericAPIView, RetrieveModelMixin):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# ListModelMixin update Students data
class StudentUpdate(GenericAPIView, UpdateModelMixin):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


# ListModelMixin Delete Students data


class StudentDetele(GenericAPIView, DestroyModelMixin):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
