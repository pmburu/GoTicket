from django.contrib import admin
from .models import (
    User, Manager, Customer,
    Favorites, Tickets_sold
)

class ManagerAdmin(admin.ModelAdmin):
    search_fields = ['username']
    list_display = [
        'username',
        'email',
        'last_name',
        'is_staff',
        'is_active',
    ]

class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['username']
    list_display = [
        'username',
        'email',
        'last_name',
        'is_active'
    ]



# Register your models here.
admin.site.register(User)
admin.site.register(Manager, ManagerAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Favorites)
admin.site.register(Tickets_sold)
