from django.urls import path, include
from rest_framework import routers

from .viewsets import UsersViewSet, ClientsViewSet, AdminsViewSet

router = routers.SimpleRouter()

router.register(r'users', UsersViewSet, basename='users')
router.register(r'admins', AdminsViewSet, basename='admins')
router.register(r'clients', ClientsViewSet, basename='clients')

urlpatterns = router.urls
