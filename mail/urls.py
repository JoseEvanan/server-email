""" Url for accounts App """
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import login
from . import views

app_name = 'accounts'

urlpatterns = [
        url(r'^send_email/$', views.send_email),
]
