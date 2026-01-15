from django.contrib import admin
from .models import CourseModel

# Register your models here.
@admin.register(CourseModel)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','name','duration','details']

