from django.urls import path
from . import views
from .views import ProgrammsDetailView
urlpatterns = [
    path("", views.index, name="index"),
    path('programms/<int:pk>/', ProgrammsDetailView.as_view(), name='programms-detail'),
]