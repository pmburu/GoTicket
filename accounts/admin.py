from typing import Set
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.forms import (
    AdminPasswordChangeForm, UserChangeForm, UserCreationForm,
)
from .models import (
    User, Manager, Customer,
    Favorites, Tickets_sold
)

from .forms import (
    CustomerCreationForm, CustomerChangeForm
)

@admin.register(Manager)
class ManagerAdmin(UserAdmin):
    fieldsets = (
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('groups',)}),
        (_('User Type'), {'fields': ('user_type',)}),
        (_('Access Credentials'), {'fields': ('username', 'password')}),
    )
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


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        disabled_fields = set()  # type: Set[str]

        if not is_superuser:
            disabled_fields |= {
                'username',
                'is_superuser',
                'user_permissions',
            }

        # Prevent non-superusers from editing their own permissions
        if (
            not is_superuser
            and obj is not None
            and obj == request.user
        ):
            disabled_fields |= {
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            }

        for f in disabled_fields:
            if f in form.base_fields:
                form.base_fields[f].disabled = True

        return form

admin.site.register(Favorites)
admin.site.register(Tickets_sold)
