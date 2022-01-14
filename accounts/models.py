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

'''
More about proxy models can be found here:
1. https://bit.ly/3Gvp7nw
2. https://bit.ly/3zVlXHa
'''
