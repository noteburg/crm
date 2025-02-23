from django.urls import reverse_lazy

from . import service, forms, models

from django.shortcuts import render, redirect
from django.views import View, generic
# Create your views here.

class CreateStudentView(View):
    def get(self, request):
        filial = service.get_admin_filial(request.user)
        groups = service.get_all_groups_from_filial(filial)
        context = {
            'groups':groups,
            'filial':filial
        }
        return render(request, 'administrator/student/create.html', context)

    def post(self, request):
        form = forms.StudentForm(request.POST)
        group_id = request.POST.get('group')

        if form.is_valid() and group_id:
            group = service.get_group_with_id(group_id)
            student = form.save()
            service.set_student_to_group(student, group)
            return redirect('home')
        return render(request, 'error.html')


class StudentTableView(View):
    def get(self, request):
        filial = service.get_admin_filial(admin=request.user)
        students = service.get_all_students_from_filial(filial)
        return render(request, 'administrator/student/table.html', {'students': students})

class CreateGroupStudentView(generic.CreateView):
    model = models.GroupStudent
    form_class = forms.GroupStudentForm
    template_name = 'administrator/group/group-student.html'
    success_url = reverse_lazy('administrator:create-group-student')
    context_object_name = 'forms'


class CreateGroupView(View):
    def get(self, request):
        filial = service.get_admin_filial(request.user)
        teachers = service.get_active_teachers_from_filial(filial)
        lessons = service.get_all_lessons_from_filial(filial)

        context = {
            'filial': filial,
            'teachers': teachers,
            'lessons': lessons
        }
        return render(request, 'administrator/group/create.html', context)


    def post(self, request):
        form = forms.GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

        return render(request, 'error.html')


class GroupsTableView(View):
    def get(self, request):
        filial = service.get_admin_filial(request.user)
        status_filter = request.GET.get('status')
        groups = service.get_all_groups_from_filial(filial, status_filter)
        context = {
            'groups':groups,
            'status':status_filter,
        }
        return render(request, 'administrator/group/table.html', context)



class CreateLessonView(View):
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

class CreateLessonTimeView(View):
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


class CreateRoomView(View):
    def get(self, request):
        filials = models.Filial.objects.all()
        return render(request, 'administrator/lesson/room/create.html', {'filials': filials})

    def post(self, request):
        form = forms.LessonRoom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'administrator/error.html')