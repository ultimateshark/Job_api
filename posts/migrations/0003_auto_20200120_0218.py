# Generated by Django 3.0.2 on 2020-01-20 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_delete_users'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Jobposts',
            new_name='AllPosts',
        ),
    ]
