from django.urls import path, include
from . import views


app_name = 'administrator'

urlpatterns = [
    path('student/create/', views.CreateStudentView.as_view(), name='student-create'),
    path('student/table/', views.StudentTableView.as_view(), name='student-table'),

    path('group/create', views.CreateGroupView.as_view(), name='create-group'),
    path('group/table/', views.GroupsTableView.as_view(), name='table-group'),
    path('group/student/create', views.CreateGroupStudentView.as_view(), name='create-group-student'),

    path('lesson/create/', views.CreateLessonView.as_view(), name='create-lesson'),
    path('lesson/create-time/', views.CreateLessonTimeView.as_view(), name='create-lesson-time'),
    path('lesson/create-room/', views.CreateRoomView.as_view(), name='create-lesson-room'),

]