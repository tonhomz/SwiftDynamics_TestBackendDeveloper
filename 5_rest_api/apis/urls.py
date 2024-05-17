from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apis.views.v1 import school, student, teacher, classroom


router = DefaultRouter()

api_v1_urls = (router.urls, 'v1')

urlpatterns = [    
    # school
    path('create_school', school.SchoolCreateView.as_view()),
    path('school_list', school.SchoolListView.as_view()),
    path('update_school/<str:name>', school.SchoolUpdateView.as_view()),
    path('delete_school/<str:name>', school.SchoolDeleteView.as_view()),

    # student
    path('create_student', student.StudentCreateView.as_view()),
    path('student_list', student.StudentListView.as_view()),
    path('update_student/<str:firstname>', student.StudentUpdateView.as_view()),
    path('delete_student/<str:firstname>', student.StudentDeleteView.as_view()),

    # teacher 
    path('create_teacher', teacher.TeacherCreateView.as_view()),
    path('teacher_list', teacher.TeacherListView.as_view()),
    path('update_teacher/<str:firstname>', teacher.TeacherUpdateView.as_view()),
    path('delete_teacher/<str:firstname>', teacher.TeacherDeleteView.as_view()),

    # classroom 
    path('create_classroom', classroom.ClassroomCreateView.as_view()),
    path('classroom_list', classroom.ClassroomListView.as_view()),
    path('update_classroom/<int:id>', classroom.ClassroomUpdateView.as_view()),
    path('delete_classroom/<int:id>', classroom.ClassroomDeleteView.as_view()),
]
