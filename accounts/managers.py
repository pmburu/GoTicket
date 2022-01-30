'''
This is a custom user manager file that creates proxy models for
the two custom user types created on the models file.

The custom manager inherits from models -> Manager class
'''

from django.db import models

class UserTypes(models.TextChoices):
    EVENT_MANAGER = 'EVENT MANAGER', 'Event Manager'
    CUSTOMER = 'CUSTOMER', 'Customer'

'''
Set a default user type when users are created then override this based
on the drop down chosen upon user registration
'''

class CustomerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user_type=UserTypes.CUSTOMER)


class EventManagerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user_type=UserTypes.EVENT_MANAGER)

    # def normalize_email(self, *args, **kwargs):
    #     return super().normalize_email(*args, **kwargs)
    #def create_user(self, email, **extra_fields):
    #
    #     extra_fields.setdefault("is_staff", True)
    #
    #     user = self.model(email=normalize_email(email))
    #     user.set_password()
    #     user.save()
    #
    #     return super().create_user(*args, **kwargs)
