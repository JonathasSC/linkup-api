from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.profile.viewsets import UsersViewSet, AdminsViewSet, ClientsViewSet

router = DefaultRouter()
router.register(r'users', UsersViewSet, basename='users')
router.register(r'admins', AdminsViewSet, basename='admins')
router.register(r'clients', ClientsViewSet, basename='clients')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('apps.auth.urls')),
]
