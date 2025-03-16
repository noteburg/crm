from django.urls import path, include
from . import views


app_name = 'administrator'

urlpatterns = [
    path('student/create/', views.CreateStudentView.as_view(), name='student-create'),
    path('student/table/', views.StudentTableView.as_view(), name='student-table'),

    path('group/create', views.CreateGroupView.as_view(), name='create-group'),
    path('group/<int:group_id>/edit', views.GroupEditView.as_view(), name='edit-group'),
    path('group/table/', views.GroupTableView.as_view(), name='table-group'),
    path('group/<int:group_id>/students/', views.GroupStudentsTableView.as_view(), name='table-group-students'),
    path('group/<int:group_id>/student/add', views.GroupStudentAddView.as_view(), name='add-student-group'),
    path('group/<int:group_id>/student/create', views.GroupStudentCreateView.as_view(), name='create-student-group'),

    path('lesson/create/', views.CreateLessonView.as_view(), name='create-lesson'),
    path('lesson/create-time/', views.CreateLessonTimeView.as_view(), name='create-lesson-time'),
    path('lesson/create-room/', views.CreateRoomView.as_view(), name='create-lesson-room'),

]