from django.db.models import (
    Model,
    CharField,
    UUIDField,
    SlugField,
    ImageField,
    ForeignKey,
    CASCADE
)

from .validators import validate_image
from django.utils.text import slugify
from django.core.validators import MinLengthValidator, MaxLengthValidator

from uuid import uuid4


class Users(Model):
    id_user: UUIDField = UUIDField(
        default=uuid4,
        editable=False,
        primary_key=True,
        null=False,
    )

    id_slug: SlugField = SlugField(
        blank=True,
        unique=True,
        editable=False
    )

    username: CharField = CharField(
        unique=True,
        max_length=25,
        validators=[
            MinLengthValidator(limit_value=2),
            MaxLengthValidator(limit_value=25)
        ]
    )

    first_name: CharField = CharField(
        max_length=50,
        validators=[
            MinLengthValidator(limit_value=2),
            MaxLengthValidator(limit_value=50)
        ]
    )

    last_name: CharField = CharField(
        max_length=50,
        validators=[
            MinLengthValidator(limit_value=2),
            MaxLengthValidator(limit_value=50)
        ]
    )

    contact: CharField = CharField(
        max_length=50,
        validators=[
            MinLengthValidator(limit_value=2),
            MaxLengthValidator(limit_value=50)
        ]
    )

    profile_image: ImageField = ImageField(
        blank=True,
        upload_to='users/profiles/',
        validators=[validate_image]
    )

    password: CharField = CharField(max_length=128)

    class Meta:
        ordering = ['username']
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def save(self, *args, **kwargs):
        if not self.id_slug:
            self.id_slug = slugify(str(self.id_user)[:10])
        super().save(*args, **kwargs)


class Clients(Model):
    id_client: UUIDField = UUIDField(
        default=uuid4,
        editable=False,
        primary_key=True
    )

    id_user = ForeignKey(
        Users,
        blank=False,
        related_name='clients',
        on_delete=CASCADE
    )

    class Meta:
        ordering = ['id_client']
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


class Admins(Model):
    id_admin: UUIDField = UUIDField(
        default=uuid4,
        editable=False,
        primary_key=True
    )

    id_user = ForeignKey(
        Users,
        blank=False,
        related_name='admins',
        on_delete=CASCADE
    )

    class Meta:
        ordering = ['id_admin']

        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'
