from django.shortcuts import render
from django.views.generic import ListView

from .models import Blog, Post


class BlogList(ListView):
    template_name = "blogs/blog_list.html"
    model = Blog


def show_blog(request, blog_id=None):
    blog = Blog.objects.get(pk=blog_id)
    return render(request, 'blogs/one_blog.html', {'blog': blog, 'posts': blog.posts.all()})


class PostList(ListView):
    template_name = "blogs/post_list.html"
    model = Post

    def get_queryset(self):
        return Post.objects.filter(blog=self.request.blog_id)


def show_post(request, blog_id=None, post_id=None):
    blog = Blog.objects.get(pk=blog_id)
    post = blog.posts.get(pk=post_id)
    return render(request, 'blogs/one_post.html', {'post': post, 'blog_id': blog_id, 'comments': post.comments.all()})
