from rest_framework import serializers

from .models import (Event, Comments)

# To do


'''
1. Serialize event models (let use model serializers since
it requires nothing but calling it)
2. Create any necesarry functions
'''

'''
This is a model serializer class found in Django Rest Framework
which helps us change dango database objects into json objects.

These objects will be useful when using async in ajax or any other JavaScript
library later.
'''
class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event

        fields = (
            'id',
            'name',
            'description',
            'location',
            'cover_image',
            'background_image',
            'time',
            'manager',
            'tickets_sold'
        )


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments

        fields = (
            'id',
            'comment',
            'created_at',
            'rating',
            'user',
            'event',
        )
