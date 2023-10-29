from django.db import models


class Student(models.Model):
    class Meta:
        ordering = ["id"]

    name = models.CharField(max_length=60)
    age = models.IntegerField()
    first_semester_grade = models.FloatField()
    second_semester_grade = models.FloatField()
    teacher_name = models.CharField(max_length=60)
    room_number = models.IntegerField()
