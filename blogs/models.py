from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Blog(models.Model):

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='belonged_blog')
    name = models.CharField(max_length=128)
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followed_blogs')
    creation_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='belonged_post')
    name = models.CharField(max_length=256)
    likes = models.IntegerField(default=0)
    users_likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_posts')
    text = models.TextField()
    blog = models.ForeignKey('Blog')
    creation_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
