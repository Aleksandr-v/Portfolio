from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . models import Job
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .forms import JobForm

# def home(request):
#     jobs = Job.objects.all()
#     page = 'home'
#     return render(request, 'jobs/home.html', {'jobs':jobs, 'page':page})

class JobListView(ListView):
    model = Job
    context_object_name = 'jobs'
    template_name = 'jobs/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'home'
        return context

def create_job(request):
    if request.method == 'POST':
        # Add request.FILES in order to upload image to the model
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            job = form.save(commit=False)
            job.image = form.cleaned_data['image']
            job.summary = form.cleaned_data['summary']
            job.save()
    else:
        form = JobForm()
    return render(request, 'jobs/create.html', {'form':form})
