from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password
from ..profile.models import Users


class UserSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = [field.name for field in Users._meta.fields]

        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
