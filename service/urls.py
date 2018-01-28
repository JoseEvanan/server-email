""" Url for accounts App """
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import login
from . import views

app_name = 'service'

urlpatterns = [
        url(r'^get_dni/$', views.get_dni),
        url(r'^get_ruc/$', views.get_ruc),
]
