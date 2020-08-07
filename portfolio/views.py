from django.shortcuts import render
from .models import Project


# Create your views here.
def home(request):
    projects = Project.objects.order_by('-date')
    return render(request, 'portfolio/home.html', {'projects': projects[:3]})


def notfound(request):
    return render(request, 'portfolio/404.html')
