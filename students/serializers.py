from rest_framework import serializers
from .models import Students
from .models import StudentPayment

class StudentSerializer(serializers.ModelSerializer):
    class Meta():
        model = Students
        fields = ['id','student_name','age','number','course_name']
        
        
class StudentPaymentSerializer(serializers.ModelSerializer):
    class Meta():
        model = StudentPayment
        fields = "__all__"
