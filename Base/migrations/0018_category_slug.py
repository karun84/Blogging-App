# Generated by Django 5.0.1 on 2024-01-26 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0017_category_blog_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
