'''
Django REST framework allows you to combine the logic
for a set of related views in a single class, called a ViewSet.
In other frameworks you may also find conceptually similar
implementations named something like 'Resources' or 'Controllers'.
'''


from rest_framework import viewsets
from .serializers import (EventSerializer, CommentSerializer)
from .models import (Event, Comments)
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class EventViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated,)
	serializer_class = EventSerializer
	queryset = Event.objects.all()

    # permission_classes = blab

def store(request):
	return render(request, 'store.html', {})
