from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Blog(models.Model):

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='belonged_blog', verbose_name="Создатель")
    name = models.CharField(max_length=128, verbose_name="Имя")
    description = models.TextField(blank=True, verbose_name="Описание")
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followed_blogs', null=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField('BlogCategory', related_name='blogs', null=True)

    def __str__(self):
        return self.name


class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='belonged_post', verbose_name="Автор")
    name = models.CharField(max_length=256, verbose_name="Заголовок")
    users_likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_posts', null=True, blank=True)
    text = models.TextField(verbose_name="Текст")
    blog = models.ForeignKey('Blog', related_name='posts', verbose_name="Блог")
    creation_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class BlogCategory(models.Model):

    name = models.CharField(max_length=150, verbose_name="Название")

    def __str__(self):
        return self.name
