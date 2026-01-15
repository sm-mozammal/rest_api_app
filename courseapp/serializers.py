from rest_framework import serializers
from .models import CourseModel


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModel
        fields = ["id", "name", "duration", "details"]
