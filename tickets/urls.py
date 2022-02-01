from django.urls import include, path
from rest_framework import routers
from .views import TicketCartViewSet

router = routers.DefaultRouter()

router.register('', TicketCartViewSet)
urlpatterns = router.urls
