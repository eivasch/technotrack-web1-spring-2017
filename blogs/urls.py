from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import BlogList, BlogDetail, PostList, PostDetail, BlogCreate, BlogUpdate, PostCreate, PostUpdate

urlpatterns = [
    url(r'^$', BlogList.as_view(), name="blog_list"),
    url(r'^(?P<blog_id>\d+)/posts/$', PostList.as_view(), name="post_list"),
    url(r'^(?P<pk>\d+)$', BlogDetail.as_view(), name="one_blog"),
    url(r'^posts/(?P<pk>\d+)$', PostDetail.as_view(), name="one_post"),
    url(r'^create$', login_required(BlogCreate.as_view()), name='blog_create'),
    url(r'^(?P<pk>\d+)/update/$', BlogUpdate.as_view(), name="blog_update"),
    url(r'^posts/create$', login_required(PostCreate.as_view()), name='post_create'),
    url(r'^posts/(?P<pk>\d+)/update/$', PostUpdate.as_view(), name="post_update"),
]
