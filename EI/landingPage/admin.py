from django.contrib import admin
from .models import Instituation,Programms,ContactMessages,Blacklist
# Register your models here.
admin.site.register(Instituation)
admin.site.register(Programms)
admin.site.register(ContactMessages)
admin.site.register(Blacklist)