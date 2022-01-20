import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating

User = get_user_model()

# Create your models here.
class Event(models.Model):

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=200)
	description = models.TextField(max_length=4000)
	location = models.CharField(max_length=50)
	cover_image = models.CharField(max_length=200)
	background_image = models.CharField(max_length=200)
	time = models.DateTimeField()
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	tickets_sold = models.IntegerField()

	class Meta:
		verbose_name = 'Event'
		verbose_name_plural = 'Events'

class Comments(models.Model):
    
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	comment = models.TextField(max_length=4000)
	created_at = models.DateTimeField()
	rating = GenericRelation(Rating, related_query_name='comment_rating')
	user = models.ForeignKey(User,on_delete=models.PROTECT)
	event = models.ForeignKey('tickets.Ticket',on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'Comment'
		verbose_name_plural = 'Comments'
