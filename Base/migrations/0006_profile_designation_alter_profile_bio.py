# Generated by Django 5.0.1 on 2024-01-12 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0005_remove_blog_image2_remove_blog_image3'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='designation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True),
        ),
    ]
