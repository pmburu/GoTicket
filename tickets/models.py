import uuid
from django.db import models
#from events.models import Event

# Create your models here.
class Ticket_type(models.Model):

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=200)
	price = models.IntegerField()
	event = models.ForeignKey('events.Event',on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'Ticket_type'
		verbose_name_plural = 'Ticket_types'

	def __str__(self):
		return self.name

class Ticket(models.Model):

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	event = models.ForeignKey('events.Event',on_delete=models.CASCADE)
	ticket_type = models.ForeignKey(Ticket_type,on_delete=models.CASCADE)
	number_of_tickets = models.IntegerField(default=0)

	class Meta:
		verbose_name = 'Ticket'
		verbose_name_plural = 'Tickets'

	def __str__(self):
		return self.ticket_type.name
