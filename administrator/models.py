from django.db import models

from employee.models import Filial, Employee


# Create your models here.

class LessonRoom(models.Model):
    filial = models.ForeignKey(Filial, on_delete=models.CASCADE, related_name='lesson_room')
    name = models.CharField(max_length=255)


# teacher
class LessonType(models.Model):
    type = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=8)


# teacher
class Lesson(models.Model):
    filial = models.ForeignKey(Filial, on_delete=models.SET_NULL, null=True, related_name='lesson')
    name = models.CharField(max_length=255)
    lesson_type = models.ForeignKey(LessonType, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class EmployeeWork(models.Model):
    filial = models.ForeignKey(Filial, on_delete=models.SET_NULL, null=True, )
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='filial')
    # salary_type = models.ForeignKey(SalaryType, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.filial}"
# teacher
class Group(models.Model):
    filial = models.ForeignKey(Filial, on_delete=models.SET_NULL, null=True, related_name='group')
    teacher = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='group')
    name = models.CharField(max_length=255)
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True, related_name='group')
    status = models.CharField(choices=(
        ('1', 'not started'),
        ('2', 'active'),
        ('3', 'inactive')
    ), max_length=1, default='1')
    teacher_per = models.IntegerField(null=True)

    def __str__(self):
        return self.name

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
    filial = models.ForeignKey(Filial, on_delete=models.SET_NULL,null=True, related_name='student')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
# student
class GroupStudent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, related_name="groups")
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name="students")
    is_active = models.BooleanField(default=True)
    is_privilege = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.group.name}"

class JournalAttendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    date = models.ForeignKey(LessonTime, on_delete=models.SET_NULL, null=True)
    is_attend = models.BooleanField(default=False)
    filial = models.ForeignKey(Filial, on_delete=models.SET_NULL,null=True, related_name='jurnal')