from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . models import Job

def home(request):
    jobs = Job.objects.all()
    page = 'home'
    return render(request, 'jobs/home.html', {'jobs':jobs, 'page':page})
