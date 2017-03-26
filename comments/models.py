# coding=utf-8

from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Comment(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='belonged_comments')
    post = models.ForeignKey('blogs.Post', related_name='comments')
    text = models.TextField(max_length=1000)
    users_likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_comments', null=True, blank=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.text[:10]
