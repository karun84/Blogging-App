# Generated by Django 5.0.1 on 2024-01-13 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0008_alter_comment_commenter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=800),
        ),
    ]
