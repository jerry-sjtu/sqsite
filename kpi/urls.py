from django.conf.urls import patterns, url

from kpi import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^chart/$', views.chart, name='chart'),
)
