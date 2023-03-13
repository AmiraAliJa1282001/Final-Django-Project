from django.forms import ModelForm, TextInput, Textarea,FileInput
from landingPage.models import Instituation,Programms
from .models import Student,Teacher,Course
from django import forms

class InstituationForm(ModelForm):
    class Meta:
        model = Instituation
        fields = ['name', 'home_title', 'home_description', 'mission', 'about_us']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'home_title': TextInput(attrs={'class': 'form-control'}),
            'home_description': Textarea(attrs={'class': 'form-control'}),
            'mission': Textarea(attrs={'class': 'form-control'}),
            'about_us': Textarea(attrs={'class': 'form-control'}),
        }

class ProgrammsCreateForm(ModelForm):
    class Meta:
        model = Programms
        fields = [ 'title', 'description', 'image']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
            'image': FileInput(attrs={'class': 'form-control-file'}),
            
        }
class ProgrammsUpdateForm(ModelForm):
    class Meta:
        model = Programms
        fields = [ 'title', 'description', 'image']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
            'image': FileInput(attrs={'class': 'form-control-file'}),
            
        }

class StudentUpdateForm(ModelForm):
    class Meta:
        model = Student
        fields = ['full_name','student_id' ,'image', 'phone', 'university', 'major', 'address', 'date_of_birth', 'gender']

    full_name = forms.CharField(label='Full name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    student_id = forms.CharField(label='Student ID', widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(label='Profile picture', widget=forms.FileInput(attrs={'class': 'form-control-file'}), required=False)
    phone = forms.CharField(label='Phone', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    university = forms.CharField(label='University', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    major = forms.CharField(label='Major', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    address = forms.CharField(label='Address', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    date_of_birth = forms.DateField(label='Date of birth', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), required=False)
    gender = forms.ChoiceField(label='Gender', widget=forms.Select(attrs={'class': 'form-control'}), choices=Student.GENDER_CHOICES, required=False)

class TeacherUpdateForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['full_name', 'teacher_id','image', 'phone', 'university', 'major']

    full_name = forms.CharField(label='Full name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    teacher_id = forms.CharField(label='Teacher ID', widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(label='Profile picture', widget=forms.FileInput(attrs={'class': 'form-control-file'}), required=False)
    phone = forms.CharField(label='Phone', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    university = forms.CharField(label='University', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    major = forms.CharField(label='Major', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'teacher', 'students', 'start_date', 'end_date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'teacher': forms.Select(attrs={'class': 'form-control'}),
            'students': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
    start_date = forms.DateField(label='start_date', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), required=False)
    end_date = forms.DateField(label='end_date', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), required=False)

class AddStudentForm(forms.Form):
    email = forms.EmailField()

from .models import Task, FileSubmission

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description', 'deadline']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
    deadline = forms.DateField(label='deadline', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), required=False)

    def __init__(self, *args, **kwargs):
        self.course = kwargs.pop('course')
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        task = super().save(commit=False)
        task.course = self.course
        if commit:
            task.save()
        return task
class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description', 'deadline']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
    deadline = forms.DateField(label='deadline', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), required=False)


from django import forms
from .models import FileSubmission

class FileSubmissionForm(forms.ModelForm):
    class Meta:
        model = FileSubmission
        fields = ['file']