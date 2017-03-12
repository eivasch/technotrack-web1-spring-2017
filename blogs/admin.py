from django.contrib import admin
from .models import Post, Blog

admin.register(Post, Blog)
