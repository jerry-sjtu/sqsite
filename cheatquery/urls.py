from django.conf.urls import patterns, url

from cheatquery import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
