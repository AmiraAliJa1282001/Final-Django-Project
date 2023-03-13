from django.urls import path
from . import views
from .views import (
    StudentDetailView,
    StudentDeleteView,
    InstituationUpdateView,
    ProgrammsCreateView,
    ProgrammsDeleteView,
    ProgrammsUpdateView,
    StudentUpdateView,
    TeacherDeleteView,
    TeacherDetailView,
    TeacherUpdateView,
    CourseCreateView,
    CourseDetailView,
    CourseDeleteView,
    CourseTeacherDetailView,
    TaskDetailView,
    CreateTaskView,
    DeleteTaskView,
    TaskUpdateView,
   
    )
 
urlpatterns = [
 path("student_registration/", views.student_registration, name="student_registration"),
 path("teacher_registration/", views.teacher_registration, name="teacher_registration"),

 path("messages_contact/", views.messages_contact, name="messages_contact"),
 path("admin-panel/", views.admin_panel, name="admin-panel"),
 path("view_students/", views.view_students, name="view_students"),
 path("view_teachers/", views.view_teachers, name="view_teachers"),
 path("view_courses/", views.view_courses, name="view_courses"),
 path('student/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
 path('teacher/<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),
 path('course/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
 path('delete-student/<int:pk>/', StudentDeleteView.as_view(), name='student-delete'),
 path('course-delete/<int:pk>/', CourseDeleteView.as_view(), name='course-delete'),
 path('delete-teacher/<int:pk>/', TeacherDeleteView.as_view(), name='teacher-delete'),
 path('delete-program/<int:pk>/', ProgrammsDeleteView.as_view(), name='program-delete'),
 path('update-instituation/<int:pk>/', InstituationUpdateView.as_view(), name='update-instituation'),
 path('program-edit/<int:pk>/', ProgrammsUpdateView.as_view(), name='program-edit'),
 path('add-program/', ProgrammsCreateView.as_view(), name='add-program'),
 path('add-course/', CourseCreateView.as_view(), name='add-course'),
 path("logout/", views.Logout, name="logout"),
  path('course/<int:course_id>/add_student/', views.add_student_to_course, name='add_student_to_course'),
 

 path('student_course_detail/<int:pk>/', views.courseStudentDetailView, name='student_course_detail'),
 path('student-edit/<int:pk>/', StudentUpdateView.as_view(), name='student-edit'),
 path("student_profile/", views.student_profile, name="student_profile"),
 path('student_courses/', views.student_courses, name='student_courses'),
 path("change_password/", views.change_password, name="change_password"),

 path('teacher_course_detail/<int:pk>/', CourseTeacherDetailView.as_view(), name='teacher_course_detail'),

 path("teacher_profile/", views.teacher_profile, name="teacher_profile"),
 path('teacher-edit/<int:pk>/', TeacherUpdateView.as_view(), name='teacher-edit'),
 path('teacher_courses/', views.teacher_courses, name='teacher_courses'),
 
 path('submit-attendance/', views.submit_attendance, name='submit_attendance'),
 path('courses/<int:course_id>/attendance/', views.view_attendance, name='view_attendance'),

path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
path('courses/<int:course_id>/create-task/', CreateTaskView.as_view(), name='create_task'),
path('tasks/<int:pk>/delete/', DeleteTaskView.as_view(), name='task_delete'),
path('tasks/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_edit'),
path('submit_file/<int:task_id>/', views.submit_file, name='submit_file'),

 path("login/", views.user_login, name="user_login"),

path('/add-to-blacklist/<int:student_id>/<int:course_id>/', views.add_to_blacklist, name='add_to_blacklist'), 
path('blacklist/', views.view_blacklist, name='view_blacklist'),

]