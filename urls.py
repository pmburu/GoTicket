from django.conf.urls import url
from django.contrib import admin
from home import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^home$', views.homepage),
]
