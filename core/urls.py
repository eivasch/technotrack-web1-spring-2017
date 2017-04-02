from django.conf.urls import url
from django.contrib.auth.views import login, logout

from .views import MainView

urlpatterns = [
    url(r'^$', MainView.as_view(), name="main"),
    url(r'^login/', login, {'template_name': 'core/login.html'}, name="login"),
    url(r'^logout/', logout, {'template_name': 'core/logout.html'}, name="logout"),
]
