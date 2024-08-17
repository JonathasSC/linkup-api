from rest_framework.serializers import ModelSerializer
from .models import Users, Clients, Admins


class UsersSerializer(ModelSerializer):
    class Meta:
        model: Users = Users
        fields = [field.name for field in Users._meta.fields]


class ClientsSerializer(ModelSerializer):
    class Meta:
        model: Clients = Clients
        fields = [field.name for field in Clients._meta.fields]


class AdminsSerializer(ModelSerializer):
    class Meta:
        model: Admins = Admins
        fields = [field.name for field in Admins._meta.fields]
