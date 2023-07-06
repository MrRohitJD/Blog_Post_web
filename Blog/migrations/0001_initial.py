# Generated by Django 4.2.2 on 2023-07-06 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=255)),
                ('head_0', models.CharField(blank=True, max_length=400)),
                ('content_0', models.TextField(blank=True, max_length=5000)),
                ('head_1', models.CharField(blank=True, max_length=400)),
                ('content_1', models.TextField(blank=True, max_length=5000)),
                ('head_2', models.CharField(blank=True, max_length=400)),
                ('content_2', models.TextField(blank=True, max_length=5000)),
                ('head_3', models.CharField(blank=True, max_length=400)),
                ('content_3', models.TextField(blank=True, max_length=5000)),
                ('head_4', models.CharField(blank=True, max_length=400)),
                ('content_4', models.TextField(blank=True, max_length=5000)),
                ('timestamp', models.DateTimeField()),
                ('slug', models.CharField(max_length=100)),
                ('image_1', models.ImageField(blank=True, default='', upload_to='Blog/images')),
                ('image_2', models.ImageField(blank=True, default='', upload_to='Blog/images')),
            ],
        ),
    ]