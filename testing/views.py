from django.shortcuts import render
import time

# Create your views here.

def home(request):
    time.sleep(40)
    return render(request, 'home.html')