from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    path('', views.homepage),
]
