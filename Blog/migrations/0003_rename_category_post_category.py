# Generated by Django 4.2.2 on 2023-07-09 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_post_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Category',
            new_name='category',
        ),
    ]
