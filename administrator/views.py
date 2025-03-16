from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST

from . import service, forms, models

from django.shortcuts import render, redirect
from django.views import View, generic

from .service import set_student_to_group


# Create your views here.

class CreateStudentView(LoginRequiredMixin, View):
    def get(self, request):
        filial = service.get_admin_filial(request.user)
        groups = service.get_all_groups_from_filial(filial)
        context = {
            'groups':groups
        }
        return render(request, 'administrator/student/create.html', context)

    def post(self, request):
        filial = service.get_admin_filial(request.user)
        form = forms.StudentForm(request.POST)
        group_id = request.POST.get('group')

        if form.is_valid() and group_id:
            group = service.get_group_with_id(group_id)
            student = form.save(commit=False)
            student.filial = filial
            student.save()
            service.set_student_to_group(student, group)
            return redirect('home')
        return render(request, 'error.html')


class StudentTableView(LoginRequiredMixin, View):
    def get(self, request):
        filial = service.get_admin_filial(admin=request.user)
        students = service.get_all_students_from_filial(filial)
        return render(request, 'administrator/student/table.html', {'students': students})


class CreateGroupView(LoginRequiredMixin, View):
    def get(self, request):
        filial = service.get_admin_filial(request.user)
        teachers = service.get_active_teachers_from_filial(filial)
        lessons = service.get_all_lessons_from_filial(filial)

        context = {
            'teachers': teachers,
            'lessons': lessons
        }
        return render(request, 'administrator/group/create.html', context)


    def post(self, request):
        filial = service.get_admin_filial(request.user)
        form = forms.GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.filial = filial
            group.save()
            return redirect('home')

        return render(request, 'error.html')


class GroupTableView(LoginRequiredMixin, View):
    def get(self, request):
        filial = service.get_admin_filial(request.user)
        status_filter = request.GET.get('status')
        groups = service.get_all_groups_from_filial(filial, status_filter)
        context = {
            'groups':groups,
            'status':status_filter,
        }
        return render(request, 'administrator/group/table.html', context)


class GroupStudentsTableView(LoginRequiredMixin, View):
    def get(self, request, group_id):
        group = service.get_group_with_id(id=group_id)
        students = service.get_group_students(group)
        context = {
            'group': group,
            'students': students
        }
        return render(request, 'administrator/group/students-table.html', context)


class GroupStudentAddView(LoginRequiredMixin, View):
    def get(self, request, group_id):
        filial = service.get_admin_filial(request.user)
        group_to_save_student = service.get_group_with_id(group_id)
        groups = service.get_all_groups_from_filial(filial)
        selected_group_id = request.GET.get('group')
        if selected_group_id and int(selected_group_id) > 0:
            group = service.get_group_with_id(int(selected_group_id))
            students = service.get_all_students_from_group(group)

        else:
            students = service.get_all_students_from_filial(filial)

        context = {
            'group_id': group_to_save_student,
            'groups': groups,
            'students': students,
            'selected_group_id': int(selected_group_id)
        }
        return render(request, 'administrator/group/student-add.html', context)

    def post(self, request, group_id):
        group = service.get_group_with_id(group_id)
        student_id = request.POST.get('student')
        if student_id != '0':
            student = service.get_student_with_id(student_id)
            set_student_to_group(student, group)
            return redirect('administrator:table-group-students', group_id=group.id)
        else:
            form = forms.StudentForm(request.POST)
            if form.is_valid():
                student = form.save(commit=False)
                student.filial = service.get_admin_filial(request.user)
                set_student_to_group(student, group)
                return redirect('administrator:table-group-students', group_id=group.id)
            return render(request, 'error.html')


class GroupStudentSetActive(View):
    def get(self, request, group_id):
        group = service.get_groupstudent_with_id(group_id)
        switch = request.GET.get('active')
        if switch == 'True':
            service.set_active_student_in_group(group, True)
        elif switch == 'False':
            service.set_active_student_in_group(group, False)
        return redirect('administrator:table-group-students', group_id=group.group.id)


class GroupStudentCreateView(View):
    def get(self, request, group_id):
        selected_group = service.get_group_with_id(group_id)
        context = {
            'selected_group': selected_group
        }
        return render(request, "administrator/group/student-create.html", context)

    def post(self, request, group_id):
        selected_group = service.get_group_with_id(group_id)
        filial = service.get_admin_filial(request.user)
        form = forms.StudentForm(request.POST)

        if form.is_valid() and selected_group:
            student = form.save(commit=False)
            student.filial = filial
            student.save()
            service.set_student_to_group(student, selected_group)
            return redirect('home')


class GroupEditView(LoginRequiredMixin , View):
    def get(self, request, group_id):
        filial = service.get_admin_filial(request.user)
        group = service.get_group_with_id(id=group_id)
        teachers = service.get_active_teachers_from_filial(filial)
        lessons = service.get_all_lessons_from_filial(filial)
        context = {
            'group': group,
            'teachers': teachers,
            'lessons': lessons,
        }
        return render(request, 'administrator/group/edit.html', context)

    def post(self, request, group_id):
        group = service.get_group_with_id(id=group_id)
        form = forms.EditGroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('administrator:table-group')
        return render(request, 'error.html')


class CreateLessonView(LoginRequiredMixin, View):
    def get(self, request):
        filials = models.Filial.objects.all()
        lesson_types = models.LessonType.objects.all()
        context = {
            'filials': filials,
            'lesson_types': lesson_types
        }
        return render(request, "administrator/lesson/create.html", context)

    def post(self, request):
        form = request.POST
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'error.html')

class CreateLessonTimeView(LoginRequiredMixin, View):
    def get(self, request):
        groups = models.Group.objects.all()
        rooms = models.LessonRoom.objects.all()
        context = {
            'groups': groups,
            'rooms': rooms
        }
        return render(request, 'administrator/lesson/create-lesson-time.html', context)

    def post(self, request):
        form = forms.LessonTime(request.POST)
        if form.is_valid():
            form.save()

        return redirect('home')


class CreateRoomView(LoginRequiredMixin, View):
    def get(self, request):
        filials = models.Filial.objects.all()
        return render(request, 'administrator/lesson/room/create.html', {'filials': filials})

    def post(self, request):
        form = forms.LessonRoom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'administrator/error.html')