from django.contrib import admin
from .models import Students
from .models import StudentPayment

# Register your models here.


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ["id", "student_name", "age", "number", "course_name"]


@admin.register(StudentPayment)
class StudentPaymentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "student_name",
        "course_name",
        "course_duration",
        "course_free",
    ]
