'''
Django REST framework allows you to combine the logic
for a set of related views in a single class, called a ViewSet.
In other frameworks you may also find conceptually similar
implementations named something like 'Resources' or 'Controllers'.
'''


from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import (EventSerializer, CommentSerializer)
from .models import (Event, Comments)

class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        me = self.request.user

        return Event.objects.filter(manager=me)
