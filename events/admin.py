from django.contrib import admin
from .models import Event, Comments

class EventAdmin(admin.ModelAdmin):
    ordering = ['date_created']
    search_fields = ['name']
    readonly_fields = ['tickets_sold']



# Register your models here.
admin.site.register(Event, EventAdmin)
admin.site.register(Comments)
