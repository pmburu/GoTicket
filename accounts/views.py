from django.shortcuts import render

# Create your views here.

import django.contrib.staticfiles


def about(request):
	return render(request, 'about.html', {})

def store(request):
	return render(request, 'store.html', {})

def login(request):
	return render(request, 'login.html', {})

def signup(request):
	return render(request, 'sign_up.html', {})

def profile(request):
	return render(request, 'profile.html', {})
