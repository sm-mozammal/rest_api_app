from django.db import models


# Create your models here.
class Students(models.Model):
    student_name = models.CharField(max_length=50)
    age = models.IntegerField()
    number = models.IntegerField(null=True, blank=True)
    course_name = models.CharField(max_length=50)
    


class StudentPayment(models.Model):
    student_name = models.CharField(max_length=50)
    course_name = models.CharField(max_length=50)
    course_duration = models.CharField(max_length=50)
    course_free = models.IntegerField()
    
