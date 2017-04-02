from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Blog(models.Model):

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='belonged_blog')
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followed_blogs', null=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField('BlogCategory', related_name='blogs', null=True)

    def __str__(self):
        return self.name


class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='belonged_post')
    name = models.CharField(max_length=256)
    users_likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_posts', null=True, blank=True)
    text = models.TextField()
    blog = models.ForeignKey('Blog', related_name='posts')
    creation_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class BlogCategory(models.Model):

    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
