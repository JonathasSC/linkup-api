# Generated by Django 5.0.6 on 2024-07-07 01:19

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id_post', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('id_slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('post_image', models.ImageField(blank=True, upload_to='posts/images/')),
                ('content', models.CharField(max_length=1024)),
                ('created_at', models.TimeField(auto_now_add=True)),
                ('updated_at', models.TimeField(auto_now=True)),
                ('user_id', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='profile.users')),
            ],
        ),
    ]