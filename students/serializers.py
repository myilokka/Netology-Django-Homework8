from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from students.models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name", "students")

    # def validate_students(self, data):
    #     quantity = len(self.initial_data['students'])
    #     if self.context['view'].action == 'update':
    #         quantity = len(self.initial_data['students']) + len(Course.objects.get(id=self.initial_data['id']).students)
    #
    #     if quantity > 20:
    #         return ValidationError('На одном курсе могут учиться не больше 20 студентов!')
    #     return self.initial_data






