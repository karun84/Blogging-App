# Generated by Django 5.0.1 on 2024-01-13 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0011_alter_comment_commenter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image1',
            field=models.ImageField(blank=True, default='default-blog.png', null=True, upload_to='image'),
        ),
    ]
