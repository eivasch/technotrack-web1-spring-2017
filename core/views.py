from django.shortcuts import render
from django.views.generic import TemplateView

from blogs.models import Blog, Post
from comments.models import Comment


class MainView(TemplateView):

    template_name = 'core/main.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['latest_articles'] = Blog.objects.all()
        context['blog_count'] = Blog.objects.all().count()
        context['post_count'] = Post.objects.all().count()
        context['comment_count'] = Comment.objects.all().count()
        return context
