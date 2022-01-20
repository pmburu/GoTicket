from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
import django.contrib.staticfiles

def home(request):
	return render(request,'index.html', {})

def about(request):
	return render(request, 'about.html', {})
