from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta
from django.urls import reverse


# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20, null=True, blank=True)
    full_name = models.CharField(max_length=50,null=True, blank=True)
    # add other fields as needed
    image = models.ImageField(upload_to="media", blank=True,null=True)
    phone = models.CharField(max_length=15 ,null=True, blank=True)
    university = models.CharField(max_length=50,null=True , blank=True)
    major = models.CharField(max_length=50 ,null=True , blank=True)
    address = models.CharField(max_length=100 ,null=True , blank=True)
    date_of_birth = models.DateField(null=True , blank=True)
    GENDER_CHOICES = (('male', 'male'),('female', 'female'), )
    gender = models.CharField(max_length=20,choices= GENDER_CHOICES ,null=True , blank=True)
    

    
 
    def __str__(self):
        return str(self.user) + " ["+str(self.full_name)+']'
    
    @property
    def get_photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/static/images/user.png"
    
    def get_absolute_url(self):
        return reverse('student_profile')

    def delete(self, *args, **kwargs):
        self.user.delete()
        super().delete(*args, **kwargs)

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher_id = models.IntegerField(null=True, blank=True )
    full_name = models.CharField(max_length=50,null=True, blank=True)
    image = models.ImageField(upload_to="media", blank=True)
    phone = models.CharField(max_length=15 ,null=True , blank=True)
    university = models.CharField(max_length=50 ,null=True , blank=True)
    major = models.CharField(max_length=50 ,null=True , blank=True)
    

    def __str__(self):
        return str(self.user) + " ["+str(self.full_name)+']'
    
    @property
    def get_photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/static/images/teacher.jpg"

    def delete(self, *args, **kwargs):
        self.user.delete()
        super().delete(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('teacher_profile')

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('view_courses')
    

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.full_name} attended {self.course.name} on {self.date} ({'Present' if self.present else 'Absent'})"

class Task(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='tasks')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='tasks_created')
    description = models.TextField(max_length=300)
    deadline = models.DateTimeField()
    has_submission = models.BooleanField(default=False)

    def __str__(self):
        return self.description[:50]
    
    def get_absolute_url(self):
        return reverse('task_detail', args=[self.id])

class FileSubmission(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='submissions')
    file = models.FileField(upload_to='submissions/')

    def __str__(self):
        return f'{self.task} by {self.student.username}'
    
    def save(self, *args, **kwargs):
        self.task.has_submission = True
        self.task.save()
        super().save(*args, **kwargs)