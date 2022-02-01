from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import (
    Ticket, TicketType, TicketCart
)

class TicketCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketCart
        fields = (
            'id',
            'ticket',
            'buyer',
            'quantity',
        )
