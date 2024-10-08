# Generated by Django 5.0.1 on 2024-01-22 18:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0015_blog_downvote_blog_upvote'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='downvote',
            field=models.ManyToManyField(blank=True, related_name='dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blog',
            name='upvote',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
