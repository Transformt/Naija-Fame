# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100)),
                ('slug', models.SlugField(help_text=b'The Slug for generating our category url')),
                ('description', models.CharField(max_length=255, verbose_name=b'Decription of Category')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100, verbose_name=b'Title')),
                ('slug', models.SlugField(help_text=b'The slug for generating our blog post url', unique=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('publish', models.BooleanField(default=False)),
                ('comment_notify', models.BooleanField(default=False)),
                ('enable_comment', models.BooleanField(default=False)),
                ('publish_datetime', models.DateTimeField(null=True)),
                ('unpublish_datetime', models.DateTimeField(null=True)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(to='fameblog.Category')),
            ],
        ),
    ]
