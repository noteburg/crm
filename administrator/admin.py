from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.Group)
admin.site.register(models.Lesson)
admin.site.register(models.LessonRoom)
admin.site.register(models.LessonTime)
admin.site.register(models.LessonType)
admin.site.register(models.EmployeeWork)
admin.site.register(models.Student)
admin.site.register(models.GroupStudent)