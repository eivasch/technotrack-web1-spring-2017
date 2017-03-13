from django.contrib import admin

from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = (
        'pk',
        'author',
        'get_post',
    )

    def get_post(self, obj):
        return obj.post


admin.site.register(Comment, CommentAdmin)
