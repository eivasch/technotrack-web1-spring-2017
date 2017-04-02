from django.contrib import admin

from .models import Post, Blog, BlogCategory


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


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

admin.site.register(Post, PostAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogCategory, CategoryAdmin)
