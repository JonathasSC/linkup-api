from uuid import uuid4

from django.db.models import (
    Model,
    CharField,
    UUIDField,
    SlugField,
    ImageField,
    ForeignKey,
    TimeField,
    CASCADE
)

from ..profile.models import Users


class Posts(Model):
    id_post: UUIDField = UUIDField(
        default=uuid4,
        editable=False,
        primary_key=True
    )

    id_slug: SlugField = SlugField(
        blank=True,
        unique=True,
        editable=False
    )

    post_image: ImageField = ImageField(
        blank=True,
        upload_to='posts/images/',
    )

    content: CharField = CharField(max_length=1024)

    created_at: TimeField = TimeField(
        auto_now_add=True,
    )

    updated_at: TimeField = TimeField(
        auto_now=True,
    )

    user_id: ForeignKey = ForeignKey(
        blank=False,
        editable=False,
        on_delete=CASCADE,
        to=Users
    )
