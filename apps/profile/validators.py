from uuid import uuid4
from typing import List
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_image(file):
    valid_mime_types: List[str] = [
        'image/jpeg',
        'image/png',
        'image/apng',
        'image/webp',
    ]

    file_mime_type = file.content_type
    if file_mime_type not in valid_mime_types:
        raise ValidationError(_('Unsuported file type'))
