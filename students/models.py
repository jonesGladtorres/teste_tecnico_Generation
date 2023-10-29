from django.db import models


class Student(models.Model):
    class Meta:
        ordering = ["id"]

    name = models.CharField(max_length=60)
    age = models.DecimalField(max_digits=2)
    first_semester_grade = models.FloatField()
    second_semester_grade = models.FloatField()
    teacher_name = models.CharField(max_length=60)
    room_number = models.IntegerField()
