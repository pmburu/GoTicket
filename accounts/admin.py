from django.contrib import admin
from .models import User, Favorites, Tickets_sold

# Register your models here.
admin.site.register(User)
admin.site.register(Favorites)
admin.site.register(Tickets_sold)
