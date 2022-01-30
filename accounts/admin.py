from typing import Set
from django.db.models import Q
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.forms import (
    AdminPasswordChangeForm, UserChangeForm, UserCreationForm,
)

from .managers import UserTypes
from .models import (
    User, Manager, Customer,
    Favorites, Tickets_sold
)
from events.models import Event, Attendance

User = get_user_model()

@admin.register(Manager)
class ManagerAdmin(UserAdmin):
    fieldsets = (
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_staff','groups',)}),
        (_('User Type'), {'fields': ('user_type',)}),
        (_('Access Credentials'), {'fields': ('username', 'password')}),
    )
    search_fields = ('username__startswith',)
    list_display = [
        'username',
        'email',
        'last_name',
        'user_type',
        'is_staff',
        'is_active',
        'last_login'
    ]
    list_per_page = 25

    # Filter only Event Managers
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        if not request.user.is_superuser:
            me = request.user.pk
            return qs.filter(Q(user_type = UserTypes.EVENT_MANAGER) & Q(pk=me))
        return qs.filter(user_type = UserTypes.EVENT_MANAGER)

@admin.register(Customer)
class CustomerAdmin(UserAdmin):
    fieldsets = (
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('groups',)}),
        (_('User Type'), {'fields': ('user_type',)}),
        (_('Access Credentials'), {'fields': ('username', 'password')}),
    )
    readonly_fields = ['user_type']
    search_fields = ('username__startswith',)
    list_display = [
        'username',
        'email',
        'last_name',
        'user_type',
        'is_active',
        'last_login'
    ]

    list_per_page = 25

    # Filter only Customers
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        if not request.user.is_superuser:
            '''
            Filter by attendance to my event where user
            is attending and is customer and the event is organized by
            me.
            '''
            customer = qs.filter(user_type = UserTypes.CUSTOMER)
            # print(customer)
            # my_event = Event.objects.filter(manager = request.user.pk)
            # event_customers = Attendance.objects.filter(
            #     Q(attendee=customer) &\
            #     Q(event=my_event)
            # )
            return customer
        return qs.filter(user_type = UserTypes.CUSTOMER)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = [
        'username',
        'last_name',
        'base_type',
        'is_superuser',
        'is_active',
        'last_login'
    ]

    # Filter only Customers
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_superuser = True)

    # def get_form(self, request, obj=None, **kwargs):
    #     form = super().get_form(request, obj, **kwargs)
    #     is_superuser = request.user.is_superuser
    #     disabled_fields = set()  # type: Set[str]
    #
    #     if not is_superuser:
    #         disabled_fields |= {
    #             'username',
    #             'is_superuser',
    #             'user_permissions',
    #         }
    #
    #     # Prevent non-superusers from editing their own permissions
    #     if (
    #         not is_superuser
    #         and obj is not None
    #         and obj == request.user
    #     ):
    #         disabled_fields |= {
    #             'is_staff',
    #             'is_superuser',
    #             'groups',
    #             'user_permissions',
    #         }
    #
    #     for f in disabled_fields:
    #         if f in form.base_fields:
    #             form.base_fields[f].disabled = True
    #
    #     return form

admin.site.register(Favorites)
admin.site.register(Tickets_sold)


# class StaffAdmin(UserAdmin):
#
#     def get_queryset(self, request):
#         qs = super(StaffAdmin, self).get_queryset(request)
#         return qs.filter(is_staff=True)
#
#     list_display = ('username', 'email', 'is_staff')
#     search_fields = ('username', 'email')
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         (_('Personal info'), {'fields': ('email',)}),
#         (_('Permissions'), {
#             'fields': ('is_active', 'is_staff', 'is_superuser', 'groups'),
#         }),
#         (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
#     )
#
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'email', 'password1', 'password2', ),
#         }),
#     )
#
#     def save_model(self, request, obj, form, change):
#         if request.user.is_superuser:
#             obj.is_staff = True
#             obj.save()
# admin.site.register(UserProxy, StaffAdmin)
