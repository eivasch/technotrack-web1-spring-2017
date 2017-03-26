from django.conf.urls import url

from .views import BlogList, BlogDetail, PostList, PostDetail

urlpatterns = [
    url(r'^$', BlogList.as_view(), name="blog_list"),
    url(r'^(?P<blog_id>\d+)/posts/$', PostList.as_view(), name="post_list"),
    url(r'^(?P<pk>\d+)$', BlogDetail.as_view(), name="one_blog"),
    url(r'^posts/(?P<pk>\d+)$', PostDetail.as_view(), name="one_post"),
]
