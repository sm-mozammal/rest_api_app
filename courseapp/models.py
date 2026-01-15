from django.db import models


# Create your models here.
class CourseModel(models.Model):
    name = models.CharField(max_length=50)
    duration = models.IntegerField()
    details = models.CharField(max_length=400)
