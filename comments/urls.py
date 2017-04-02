from django.conf.urls import url

from .views import CommentFormView

urlpatterns = [
    url('^my_form/$', CommentFormView.as_view(), name='comment_form'),
]
