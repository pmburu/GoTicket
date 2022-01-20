import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Import custom manager classes
from .managers import (
UserTypes, CustomerManager, EventManagerManager
)

'''
Custom user model inheriting from the abtract user since
there is no major Django default user settings being changed.

For reference see:
1. https://bit.ly/3zWfZ8M
2. https://bit.ly/34RB6Og
'''

class User(AbstractUser):

    # Default user type --> invoked upon registration and updated on choices
    base_type = UserTypes.CUSTOMER

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_type = models.CharField(
        _('User Type'), max_length=13, choices=UserTypes.choices, default=base_type
    )

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

    '''
    Save changes made to the user 'upon registration' by invoking the
    parent save method that is shipped with the Django AbstractUser class.
    '''
    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.base_type
        return super().save(*args, **kwargs)

class EventManagerDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='event_manager_details')
    # tickets_sold = models.ForeignKey(Tickets, on_delete=models.PROTECT,  related_name='tickets_sold_by') -- awaiting the tickets model to be created

class Manager(User):

    base_type = UserTypes.EVENT_MANAGER
    objects = EventManagerManager()

    @property
    def manager_details(self):
        return self.eventmanagerdetails

    '''
    Tell Django database engine to treat this class as a proxy model.
    No table created, hence number of queries are reduced, perfomance increased
    '''

    class Meta:
        proxy = True

class Customer(User):

    base_type = UserTypes.CUSTOMER
    objects = CustomerManager()

    '''
    Tell Django database engine to treat this class as a proxy model.
    No table created, hence number of queries are reduced, perfomance increased
    '''

    class Meta:
        proxy = True

class Tickets_sold(models.Model):
    
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	total = models.IntegerField()

class Event(models.Model):

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=200)
	description = models.TextField(max_length=4000)
	location = models.CharField(max_length=50)
	cover_image = models.CharField(max_length=200)
	background_image = models.CharField(max_length=200)
	time = models.DateTimeField()
	user_id = models.ForeignKey(User,on_delete=models.CASCADE)
	tickets_sold = models.IntegerField()

class Ticket_type(models.Model):

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=200)
	price = models.IntegerField()
	event_id = models.ForeignKey(Event,on_delete=models.CASCADE)

class Ticket(models.Model):

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	event_id = models.ForeignKey(Event,on_delete=models.CASCADE)
	ticket_type_id = models.ForeignKey(Ticket_type,on_delete=models.CASCADE)

class Comments(models.Model):
    
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	comment = models.TextField(max_length=4000)
	created_at = models.DateTimeField()
	score = models.IntegerField(max_length=5)
	user_id = models.ForeignKey(User,on_delete=models.CASCADE)
	event_id = models.ForeignKey(Ticket,on_delete=models.CASCADE)

class Favorites(models.Model):

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user_id = models.ForeignKey(User,on_delete=models.CASCADE)
	event_id = models.ForeignKey(Ticket,on_delete=models.CASCADE)

'''
More about proxy models can be found here:
1. https://bit.ly/3Gvp7nw
2. https://bit.ly/3zVlXHa
'''
