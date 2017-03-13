from django.contrib import admin

from .models import Post, Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'description',
    )


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'blog',
    )


admin.site.register(Post, PostAdmin)
admin.site.register(Blog, BlogAdmin)

