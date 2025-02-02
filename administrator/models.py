from django.db import models

from employee.models import Filial, Employee


# Create your models here.

class LessonRoom(models.Model):
    name = models.CharField(max_length=255)


# teacher
# class SalaryType(models.Model):
#     type = models.IntegerField()


# teacher
class LessonType(models.Model):
    type = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=8)


# teacher
class Lesson(models.Model):
    filial = models.ForeignKey(Filial, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    lesson_type = models.ForeignKey(LessonType, on_delete=models.SET_NULL, null=True)


class EmployeeWork(models.Model):
    filial = models.ForeignKey(Filial, on_delete=models.SET_NULL, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    # salary_type = models.ForeignKey(SalaryType, on_delete=models.SET_NULL, null=True)


# teacher
class Group(models.Model):
    filial = models.ForeignKey(Filial, on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=False)
    teacher_per = models.IntegerField()


class LessonTime(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='lesson_time')
    date = models.DateField(blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.ForeignKey(LessonRoom, on_delete=models.SET_NULL, null=True, related_name='lesson_time')


# student
class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)


# student
class GroupStudent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=False)
    is_privilege = models.BooleanField(default=False)


class JournalAttendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    date = models.ForeignKey(LessonTime, on_delete=models.SET_NULL, null=True)
    is_attend = models.BooleanField(default=False)
