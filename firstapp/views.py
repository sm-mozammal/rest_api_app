from django.shortcuts import render
from .models import Teacher
from .serializers import TeacherSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser


# Create your views here.


# QuerySet
def teacher_info(request):
    # complex data
    teacher = Teacher.objects.all()
    print("teacher : ", teacher)
    # python dict
    serializer = TeacherSerializers(teacher, many=True)
    print("serializer : ", serializer)
    # convert to json
    json_data = JSONRenderer().render(serializer.data)
    print("json data : ", json_data)
    # json sent to fronend
    return HttpResponse(json_data, content_type="application/json")


# modle instance
def teacher_by_id(request, pk):
    # complex data
    teacher = Teacher.objects.get(id=pk)
    # python dict
    serializer = TeacherSerializers(teacher)
    # convert to json
    json_data = JSONRenderer().render(serializer.data)
    # json sent to fronend
    return HttpResponse(json_data, content_type="application/json")


# create or save


@csrf_exempt
def teacher_create(request):
    if request.method == "POST":
        json_data = request.body
        # json to stream convert
        stream_data = io.BytesIO(json_data)
        # stream to python convert
        pythondata = JSONParser().parse(stream_data)
        # python to complex convert
        serializer_data = TeacherSerializers(data=pythondata)
        if serializer_data.is_valid():
            serializer_data.save()
            response = {"message": "Successfully insert data"}
            json = JSONRenderer().render(response)
            return HttpResponse(json, content_type="application/json")
        json = JSONRenderer().render(serializer_data.errors)
        return HttpResponse(json, content_type="application/json")

    if request.method == "PUT":
        json_data = request.body
        # json ot stream
        stream_data = io.BytesIO(json_data)
        # stream to python
        pythondata = JSONParser().parse(stream_data)

        t_id = pythondata.get("id")

        teacher = Teacher.objects.get(id=t_id)

        serializer = TeacherSerializers(teacher, data=pythondata, partial=True)

        if serializer.is_valid():
            serializer.save()
            response = {"message": "Successfully updated data"}
            json = JSONRenderer().render(response)
            return HttpResponse(json, content_type="application/json")
        json = JSONRenderer().render(serializer_data.errors)
        return HttpResponse(json, content_type="application/json")
