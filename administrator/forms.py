from django import forms
from . import models

class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = ['first_name', 'last_name', 'phone', 'filial']


class GroupStudentForm(forms.ModelForm):
    class Meta:
        model = models.GroupStudent
        fields = ['student', 'group', 'is_privilege']
        widgets = {
            'student' : forms.Select(attrs={'class': 'row form-group'}),
            'group' : forms.Select(attrs={'class': 'row form-group'}),
            'is_privilege' : forms.CheckboxInput(attrs={'class': 'row form-check-input'}),
        }


class GroupForm(forms.ModelForm):
    class Meta:
        model = models.Group
        fields = ['filial', 'teacher', 'name', 'lesson']


class Lesson(forms.ModelForm):
    class Meta:
        model = models.Lesson
        fields = ['filial', 'name', 'lesson_type']


class LessonTime(forms.ModelForm):
    class Meta:
        model = models.LessonTime
        fields = '__all__'


class LessonRoom(forms.ModelForm):
    class Meta:
        model = models.LessonRoom
        fields = ['filial', 'name']