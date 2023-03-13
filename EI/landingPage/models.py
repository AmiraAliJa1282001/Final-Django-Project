from django.db import models
from django.urls import reverse
# Create your models here.
class SingletonModel(models.Model):
    def save(self, *args,**kwargs):
        self.pk=1
        super().save(*args,**kwargs)

class Instituation (SingletonModel):
    name = models.CharField(max_length=100)
    home_title = models.CharField(max_length=100)
    home_description = models.CharField(max_length=300)
    mission = models.CharField(max_length=300)
    about_us = models.CharField(max_length=500)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('admin-panel')

class Programms(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to="media", blank=True)

    def __str__(self):
        return str(self.title)
    
    def get_photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/static/images/backg1.jpg"

    def get_absolute_url(self):
        return reverse('admin-panel')

class ContactMessages (models.Model):
    full_name=models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message_content = models.CharField(max_length=500)

    def __str__(self):
        return str(self.full_name)

class Blacklist(models.Model): 
     student = models.ForeignKey('education.Student', on_delete=models.CASCADE) 
     teacher_rating = models.IntegerField() 
     created_at = models.DateTimeField(auto_now_add=True) 
 
     def __str__(self): 
        return f"{self.student} - {self.teacher_rating}"



    

