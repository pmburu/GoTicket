import uuid
from pathlib import Path
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating

User = get_user_model()


"""Upload helper function - to save image as id - filename"""

def image_upload(instance, filename):
    path = Path(filename)
    return "event/{}{}".format(uuid.uuid4(), path.suffix)

# Create your models here.
class Event(models.Model):

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=200)
	description = models.TextField(max_length=4000)
	location = models.CharField(max_length=50)
	cover_image = models.ImageField(upload_to=image_upload)
	background_image = models.ImageField(upload_to=image_upload)
	time = models.DateTimeField()
	manager = models.ForeignKey(User,on_delete=models.CASCADE)
	tickets_sold = models.IntegerField(default=0)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Event'
		verbose_name_plural = 'Events'

	def __str__(self):
		return self.name

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
