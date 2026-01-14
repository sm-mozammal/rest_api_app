from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Students
from .serializers import StudentSerializer


# Create your views here.
@api_view(["GET", "POST"])
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
