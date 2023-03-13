from django.shortcuts import render, redirect
from .models import Instituation,Programms
from django.views.generic.detail import DetailView
from django.utils import timezone
from .forms import ContactMessagesForm
# Create your views here.
def index(request):
    form = ContactMessagesForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
            return redirect("index")

    inst = Instituation.objects.get(pk=1)
    all_programs = Programms.objects.all()
    
    return render(request, "landingPage/index.html" , {"instituation": inst, "programs": all_programs, "form": form,})

class ProgrammsDetailView(DetailView):

    model = Programms

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context