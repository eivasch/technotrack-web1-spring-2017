from django.views.generic import ListView, DetailView

from .models import Blog, Post


class BlogList(ListView):
    template_name = "blogs/blog_list.html"
    model = Blog


class BlogDetail(DetailView):

    model = Blog
    template_name = 'blogs/one_blog.html'


class PostList(ListView):
    template_name = "blogs/post_list.html"
    model = Post

    def get_queryset(self):
        return Post.objects.filter(blog=self.request.blog_id)


class PostDetail(DetailView):
    template_name = 'blogs/one_post.html'
    model = Post
