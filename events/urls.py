'''
Register the viewset with a router,
and allow the urlconf to be automatically generated
'''

from rest_framework.routers import DefaultRouter
from .views import (EventViewSet)
from django.urls import path, include
from events import views

router = DefaultRouter()
router.register('', EventViewSet, basename='event')
urlpatterns = router.urls

