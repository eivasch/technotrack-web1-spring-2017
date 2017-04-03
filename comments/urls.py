from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import CommentFormView

urlpatterns = [
    url('^my_form/$', login_required(CommentFormView.as_view()), name='comment_form'),
]
