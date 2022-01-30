from django.contrib.auth import get_user_model, forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Importing django.forms under a special namespace
from django import forms as d_forms

from .managers import UserTypes
from .models import Customer, Manager

User = get_user_model()

class CustomerCreationForm(forms.UserCreationForm):

    class Meta:
        model = Customer
        fields = ('email',)


class CustomerChangeForm(forms.UserChangeForm):

    class Meta:
        model = Customer
        fields = ('email',)

# class UserChangeForm(forms.UserChangeForm):
#     class Meta(forms.UserChangeForm.Meta):
#         model = User
#
#
# class UserCreationForm(forms.UserCreationForm):
#
#     error_message = forms.UserCreationForm.error_messages.update(
#         {
#             "duplicate_username": _(
#                 "This username has already been taken."
#             )
#         }
#     )
#
#     class Meta(forms.UserCreationForm.Meta):
#         model = User
#
#     def clean_username(self):
#         username = self.cleaned_data["username"]
#
#         try:
#             User.objects.get(username=username)
#         except User.DoesNotExist:
#             return username
#
#         raise ValidationError(
#             self.error_messages["duplicate_username"]
#         )
#
# # SignupForm inherits from django-allauth's SignupForm
# class SignupForm(forms.UserCreationForm):
#
#     # Specify a choice field that matches the choice field on our user model
#     type = d_forms.ChoiceField(choices=[
#         ('EVENT_MANAGER', 'Event Manager'),
#         ('CUSTOMER', 'Customer')
#     ])
#
#     # Override the init method
#     def __init__(self, *args, **kwargs):
#         # Call the init of the parent class
#         super().__init__(*args, **kwargs)
#         # Remove autofocus because it is in the wrong place
#         del self.fields['username'].widget.attrs["autofocus"]
#
#     # Put in custom signup logic
#     def custom_signup(self, request, user):
#         # Set the user's type from the form reponse
#         user.user_type = self.cleaned_data["type"]
#         # Save the user's type to their database record
#         user.save()
