# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 21:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photo', '0003_auto_20161025_1046'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoDislike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='photo',
            name='dislike_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='photo',
            name='like_users',
            field=models.ManyToManyField(related_name='photo_set_like_users', through='photo.PhotoLike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='album',
            name='img_cover',
            field=models.ImageField(blank=True, upload_to='album'),
        ),
        migrations.AddField(
            model_name='photodislike',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photo.Photo'),
        ),
        migrations.AddField(
            model_name='photodislike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='photo',
            name='dislike_users',
            field=models.ManyToManyField(related_name='photo_set_dislike_users', through='photo.PhotoDislike', to=settings.AUTH_USER_MODEL),
        ),
    ]
