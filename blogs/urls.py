from django.conf.urls import url

from .views import BlogList, show_blog, show_post, PostList

urlpatterns = [
    url(r'^$', BlogList.as_view(), name="blog_list"),
    url(r'^(?P<blog_id>\d+)/posts/$', PostList.as_view(), name="post_list"),
    url(r'^(?P<blog_id>\d+)$', show_blog, name="one_blog"),
    url(r'^(?P<blog_id>\d+)/posts/(?P<post_id>\d+)$', show_post, name="one_post"),
]
