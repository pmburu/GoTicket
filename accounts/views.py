from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
import django.contrib.staticfiles

def home(request):
	return render(request,'index.html', {})

def about(request):
	return render(request, 'about.html', {})

def login(request):
	return render(request, 'login.html', {})

def signup(request):
	return render(request, 'sign_up.html', {})

def profile(request):
	return render(request, 'profile.html', {})

def store(request):
	return render(request, 'store.html', {})

