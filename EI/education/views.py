from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.contrib.auth.models import User
from .models import Student,Teacher,Course,Attendance,Task,FileSubmission
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView,UpdateView,CreateView
from django.utils import timezone
from landingPage.models import Instituation,Programms,ContactMessages,Blacklist
from django.contrib import messages
from .forms import AddStudentForm,TaskUpdateForm,FileSubmissionForm
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from .forms import (
    InstituationForm,
    ProgrammsCreateForm,
    ProgrammsUpdateForm,
    StudentUpdateForm,
    TeacherUpdateForm,
    CourseCreateForm,
)
from .utils import is_student, is_teacher

# Create your views here.
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url = '/admin_login')
def student_registration(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            passnotmatch = True
            return render(request, "education/student/student_registration.html", {'passnotmatch':passnotmatch})

        user = User.objects.create_user(username=username, email=email, password=password,first_name=first_name, last_name=last_name)
        student = Student.objects.create(user=user , full_name= first_name+" "+last_name )
        user.save()
        student.save()
        alert = True
        return render(request, "education/student/student_registration.html", {'alert':alert})
    return render(request, "education/student/student_registration.html")

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url = '/admin_login')
def teacher_registration(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            passnotmatch = True
            return render(request, "education/teacher/teacher_registration.html", {'passnotmatch':passnotmatch})

        user = User.objects.create_user(username=username, email=email, password=password,first_name=first_name, last_name=last_name)
        teacher = Teacher.objects.create(user=user, full_name= first_name+" "+last_name )
        user.save()
        teacher.save()
        alert = True
        return render(request, "education/teacher/teacher_registration.html", {'alert':alert})
    return render(request, "education/teacher/teacher_registration.html")


@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url = '/admin_login')
def admin_panel (request):
    inst = Instituation.objects.get(pk=1)
    all_programs = Programms.objects.all()
    return render(request, "education/admin/admin-panel.html", {"instituation":inst,"programs": all_programs,})

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url = '/admin_login')
def messages_contact (request):
    messages = ContactMessages.objects.all()
    return render(request, "education/admin/messages_contact.html", {"messages":messages})

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url = '/admin_login')
def view_students(request):
    students = Student.objects.all()
    return render(request, "education/admin/view_students.html", {'students':students})

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url = '/admin_login')
def view_teachers(request):
    teachers = Teacher.objects.all()
    return render(request, "education/admin/view_teachers.html", {'teachers':teachers})

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url = '/admin_login')
def view_courses(request):
    courses = Course.objects.all()
    return render(request, "education/admin/view_courses.html", {'courses':courses})

@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class StudentDetailView(DetailView):
    model = Student
    login_required = True
    template_name = 'education/admin/student_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class TeacherDetailView(DetailView):
    model = Teacher
    login_required = True
    template_name = 'education/admin/teacher_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class CourseDetailView(DetailView):
    model = Course
    login_required = True
    template_name = 'education/admin/course_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class StudentDeleteView(DeleteView):
    model = Student
    login_required = True
    template_name = 'education/admin/confirm_delete.html'
    success_url = reverse_lazy('view_students')

@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class CourseDeleteView(DeleteView):
    model = Course
    login_required = True
    template_name = 'education/admin/confirm_delete.html'
    success_url = reverse_lazy('view_courses')

@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class TeacherDeleteView(DeleteView):
    model = Teacher
    login_required = True
    template_name = 'education/admin/confirm_delete.html'
    success_url = reverse_lazy('view_teachers')

def Logout(request):
    logout(request)
    return redirect ("/")

@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class InstituationUpdateView(UpdateView):
    model = Instituation
    login_required = True
    form_class = InstituationForm
    template_name = 'education/admin/update_instituation.html'

@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class ProgrammsCreateView(CreateView):
    model = Programms
    login_required = True
    form_class = ProgrammsCreateForm
    template_name = 'education/admin/add-program.html'

@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class ProgrammsDeleteView(DeleteView):
    model = Programms
    login_required = True
    template_name = 'education/admin/confirm_delete.html'
    success_url = reverse_lazy('admin-panel')

@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class ProgrammsUpdateView(UpdateView):
    model = Programms
    login_required = True
    form_class = ProgrammsUpdateForm
    template_name = 'education/admin/update_programms.html'

@user_passes_test(is_student)
@login_required(login_url = '/student_login')
def student_profile(request ):
    return render(request, "education/student/student_profile.html")

@method_decorator(login_required(login_url='/student_login'), name='dispatch')
@method_decorator(user_passes_test(is_student), name='dispatch')
class StudentUpdateView(UpdateView):
    model = Student
    login_required = True
    form_class = StudentUpdateForm
    template_name = 'education/student/update_Student.html'

@user_passes_test(is_student)
@login_required(login_url = '/teacher_login')
def student_courses(request):
    student = Student.objects.get(id=request.user.student.id)
    return render(request, "education/student/student_courses.html", {"student": student})

def change_password(request):
    if request.method == "POST":
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(current_password):
                u.set_password(new_password)
                u.save()
                alert = True
                return render(request, "index.html")
            else:
                currpasswrong = True
                return render(request, "change_password.html", {'currpasswrong':currpasswrong})
        except:
            pass
    return render(request, "education/change_password.html")


@user_passes_test(is_teacher)
@login_required(login_url = '/teacher_login')
def teacher_profile(request ):
    return render(request, "education/teacher/teacher_profile.html")

@method_decorator(login_required(login_url='/teacher_login'), name='dispatch')
@method_decorator(user_passes_test(is_teacher), name='dispatch')
class TeacherUpdateView(UpdateView):
    model = Teacher
    login_required = True
    form_class = TeacherUpdateForm
    template_name = 'education/teacher/update_teacher.html'


@method_decorator(login_required(login_url='/admin_login'), name='dispatch')
@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class CourseCreateView(CreateView):
    model = Course
    login_required = True
    form_class = CourseCreateForm
    template_name = 'education/admin/add-course.html'

@login_required(login_url = '/teacher_login')
@user_passes_test(is_teacher)
def teacher_courses(request):
     courses = Course.objects.filter(teacher= request.user.teacher.id)
     return render(request, "education/teacher/teacher_courses.html", {"courses": courses})


@method_decorator(login_required(login_url='/teacher_login'), name='dispatch')
@method_decorator(user_passes_test(is_teacher), name='dispatch')
class CourseTeacherDetailView(DetailView):
    model = Course
    login_required = True
    template_name = 'education/teacher/teacher_course_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        tasks = Task.objects.filter(course=self.object)
        context['tasks'] = tasks
        return context

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url = '/admin_login')
def add_student_to_course(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        form = AddStudentForm(request.POST)
        if form.is_valid():
            student_email = form.cleaned_data['email']
            try:
                user= User.objects.get(email=student_email)
                student = Student.objects.get(user= user.id)
                course.students.add(student)
                messages.success(request, f'Student "{student}" added to course "{course}"')
                return redirect('course_detail', pk=course.id)
            except Student.DoesNotExist:
                messages.error(request, f'No student found with email "{student_email}"')
    else:
        form = AddStudentForm()
    return render(request, 'education/admin/add_student_to_course.html', {'course': course, 'form': form})

@user_passes_test(is_student)
@login_required(login_url = '/student_login')
def courseStudentDetailView(request, pk):
    student = request.user.student
    course = Course.objects.get(id= pk)
    tasks = Task.objects.filter(course=course)
    return render(request, "education/student/student_course_detail.html", {"student":student,"course": course,"tasks":tasks,})


@user_passes_test(is_student)
@login_required(login_url = '/student_login')
def submit_attendance(request):
    # Retrieve the student ID and course ID from the URL parameters
    student_id = request.GET.get('student_id')
    course_id = request.GET.get('course_id')
    
    # Get the student and course objects from the database
    student = get_object_or_404(Student, id=student_id)
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        # Process the attendance form submission
        date = timezone.now().date()
       
        attendance = Attendance.objects.create(student=student, course=course, date=date, present=True)
        context = {'attendance': attendance}
        return render(request, 'education/student/attendance_confirmation.html', context)
    else:
        # Render the attendance form, pre-populating the hidden input fields with the student ID and course ID
        context = {
            'student': student,
            'course': course,
        }
        return render(request, 'education/student/submit_attendance.html', context)

@user_passes_test(is_teacher)
@login_required(login_url = '/teacher_login')
def view_attendance(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    attendance_records = Attendance.objects.filter(course=course)

    context = {
        'course': course,
        'attendance_records': attendance_records,
    }

    return render(request, 'education/teacher/view_attendance.html', context)

# @method_decorator(login_required(login_url='/teacher_login'), name='dispatch')
# @method_decorator(user_passes_test(is_teacher), name='dispatch')


class TaskDetailView(DetailView):
    model = Task
    template_name = 'education/teacher/task_detail.html'
    login_required = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = self.object
        context['submissions'] = task.submissions.all()
        return context

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

from .models import Course, Task, FileSubmission
from .forms import TaskForm, FileSubmissionForm

@method_decorator(login_required, name='dispatch')
class CreateTaskView(View):
    def get(self, request, course_id):
        course = get_object_or_404(Course, id=course_id )
        form = TaskForm(course=course)
        return render(request, 'education/teacher/create_task.html', {'form': form, 'course': course})

    def post(self, request, course_id):
        course = get_object_or_404(Course, id=course_id, teacher=request.user.teacher)
        form = TaskForm(request.POST, course=course)
        if form.is_valid():
            task = form.save(commit=False)
            task.course = course
            task.teacher = request.user.teacher
            task.save()
            return redirect('teacher_course_detail', pk=course.id)
        return render(request, 'education/teacher/create_task.html', {'form': form, 'course': course})


@method_decorator(login_required, name='dispatch')
class DeleteTaskView(DeleteView):
    model = Task
    login_required = True
    template_name = 'education/admin/confirm_delete.html'
    success_url = reverse_lazy('teacher_course_detail')

    def get_success_url(self):
        return reverse_lazy('teacher_course_detail', kwargs={'pk': self.object.course.pk})


@method_decorator(login_required, name='dispatch')
class TaskUpdateView(UpdateView):
    model = Task
    login_required = True
    form_class = TaskUpdateForm
    template_name = 'education/teacher/edit_task.html'


def submit_file(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    student = request.user.student
    if request.method == 'POST':
        form = FileSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            file_submission = form.save(commit=False)
            file_submission.task = task
            file_submission.student = student
            file_submission.save()
            messages.success(request, 'File submission successful.')
            return redirect('student_course_detail', pk=task.course_id)
    else:
        form = FileSubmissionForm()
    return render(request, 'education/student/submit_file.html', {'form': form, 'task': task})


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return redirect("/admin-panel")
            elif is_student(request.user):
                return redirect("student_profile")
            elif is_teacher(request.user):
                return redirect("teacher_profile")
            else:
                return HttpResponse("You are not authorized to access this page.")
        else:
            alert = True
            return render(request, "education/login.html", {'alert':alert})
    return render(request, "education/login.html")

def add_to_blacklist(request, student_id,course_id): 
    if request.method == 'POST': 
        teacher_rating = int(request.POST.get('teacher_rating')) 
        if teacher_rating < 5: 
            student = Student.objects.get(id=student_id) 
            blacklist = Blacklist.objects.create(student=student, teacher_rating=teacher_rating) 
            return redirect('teacher_course_detail', pk=course_id ) # Or redirect to a success page 
    else: 
        student = Student.objects.get(id=student_id) 
        return render(request, 'education/teacher/add_to_blacklist.html', {'student': student})

def view_blacklist(request): 
    blacklist_list = Blacklist.objects.all() 
    return render(request, 'education/admin/blacklist_list.html', {'blacklist_list': blacklist_list}) 
