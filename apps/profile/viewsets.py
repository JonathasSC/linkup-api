from rest_framework import viewsets
from rest_framework.response import Response

from .models import Users, Clients, Admins
from .serializers import UsersSerializer, ClientsSerializer, AdminsSerializer

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class UsersViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = UsersSerializer
    queryset = Users.objects.all()

    @method_decorator(cache_page(6))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(6))
    def retrive(self, request, *args, **kwargs):
        return super().retrive(request, *args, **kwargs)

    @method_decorator(cache_page(6))
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer
    permission_classes = (IsAuthenticated, )

    @method_decorator(cache_page(6))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(6))
    def retrive(self, request, *args, **kwargs):
        return super().retrive(request, *args, **kwargs)

    @method_decorator(cache_page(6))
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class AdminsViewSet(viewsets.ModelViewSet):
    queryset = Admins.objects.all()
    serializer_class = AdminsSerializer
    permission_classes = (IsAuthenticated, )

    @method_decorator(cache_page(6))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(6))
    def retrive(self, request, *args, **kwargs):
        return super().retrive(request, *args, **kwargs)

    @method_decorator(cache_page(6))
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
