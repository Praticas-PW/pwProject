# Generated by Django 4.2.2 on 2023-06-15 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]
