from django.contrib import admin

from students.models import Course, Student


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass

