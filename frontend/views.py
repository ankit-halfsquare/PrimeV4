from django.shortcuts import render

# Create your views here.


def webix(request):
    return render(request, 'frontend/webix.html')


def home(request):
    return render(request, 'home/home.html')