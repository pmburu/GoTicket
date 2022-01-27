'''
Django REST framework allows you to combine the logic
for a set of related views in a single class, called a ViewSet.
In other frameworks you may also find conceptually similar
implementations named something like 'Resources' or 'Controllers'.
'''

from rest_framework import viewsets
from django.shortcuts import render

def homepage(request):
	return render(request, 'index.html')
