from django.conf.urls import include, url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.main),
    url(r'^params/$', views.params, name="params"),
    url(r'^result/$', views.results, name="results"), 
]
