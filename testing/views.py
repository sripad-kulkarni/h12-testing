from django.shortcuts import render
import time

# Create your views here.

def home(request):
    time.sleep(40)
    return render(request, 'home.html')

def office(request):
    return render(request, 'office.html')

def school(request):
    return render(request, 'school.html')