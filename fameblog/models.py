from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.db.models import permalink
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
#from django.core.files.storage import default_storage as storage
from django.core.validators import RegexValidator
# Create your models here.

class Category(models.Model):
	title = models.CharField(unique=True, max_length=100)
	slug = models.SlugField(help_text='The Slug for generating our category url')
	description = models.CharField(max_length=255, verbose_name='Decription of Category')
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_updated = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.title

	# @permalink
	# def get_absolute_url(self):
	# 	return ('view_blog_category', None, {'slug': self.slug})


class Post(models.Model):
	author = models.ForeignKey(User)
	category = models.ForeignKey(Category)
	title = models.CharField(verbose_name="Title", max_length=100, unique=True)
	slug = models.SlugField(unique=True, help_text="The slug for generating our blog post url")
	content = RichTextField()
	publish = models.BooleanField(default=False)
	comment_notify = models.BooleanField(default=False)
	enable_comment = models.BooleanField(default=False)
	publish_datetime = models.DateTimeField(null=True)
	unpublish_datetime = models.DateTimeField(null=True)
	datetime_created = models.DateTimeField(auto_now_add=True)
	datetime_updated = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.title

	







