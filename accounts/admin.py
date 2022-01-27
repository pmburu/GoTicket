from typing import Set
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    User, Manager, Customer,
    Favorites, Tickets_sold
)

class ManagerAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields' : ('username', 'password')}),
    )
    search_fields = ('username__startswith',)
    list_display = [
        'username',
        'email',
        'last_name',
        'is_staff',
        'is_active',
    ]
    list_per_page = 25

class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['username']
    list_display = [
        'username',
        'email',
        'last_name',
        'is_active'
    ]


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

# admin.site.register(User, UserAdmin)
admin.site.register(Manager, ManagerAdmin)
# admin.site.register(Customer, CustomerAdmin)
admin.site.register(Favorites)
admin.site.register(Tickets_sold)
