from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import resolve_url

from .models import Blog, Post
from core.models import User
from .forms import BlogForm, PostForm
from comments.forms import CommentForm


####################
# *** Blog Views ***

class BlogList(ListView):
    template_name = "blogs/blog_list.html"
    model = Blog
    paginate_by = 5


class BlogDetail(DetailView):

    model = Blog
    template_name = 'blogs/one_blog.html'


class BlogCreate(CreateView):
    template_name = 'blogs/create_blog.html'
    model = Blog
    form_class = BlogForm

    def get_success_url(self):
        return resolve_url('blogs:blog_list')

    def form_valid(self, form):
        blog = form.save(commit=False)
        blog.owner = User.objects.get(pk=self.request.user.pk)
        blog.save()
        return super(BlogCreate, self).form_valid(form)


class BlogUpdate(UpdateView):
    template_name = 'blogs/update_blog.html'
    model = Blog
    form_class = BlogForm

    def get_success_url(self):
        return resolve_url('blogs:one_blog', pk=self.object.pk)

    def get_queryset(self):
        return Blog.objects.filter(author=self.request.user)


####################
# *** Post Views ***

class PostList(ListView):
    template_name = "blogs/post_list.html"
    model = Post

    def get_queryset(self):
        return Post.objects.filter(blog=self.request.blog_id)


class PostDetail(DetailView):
    template_name = 'blogs/one_post.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['form'] = CommentForm
        return context


class PostCreate(CreateView):
    template_name = 'blogs/create_post.html'
    model = Post
    form_class = PostForm

    def get_success_url(self):
        return resolve_url('blogs:one_blog', pk=self.object.blog.pk)

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = User.objects.get(pk=self.request.user.pk)
        post.save()
        return super(PostCreate, self).form_valid(form)


class PostUpdate(UpdateView):
    template_name = 'blogs/update_post.html'
    model = Post
    form_class = PostForm

    def get_success_url(self):
        return resolve_url('blogs:one_blog', pk=self.object.blog.pk)

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)
