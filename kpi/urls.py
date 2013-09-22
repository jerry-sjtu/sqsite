from django.conf.urls import patterns, url

from kpi import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^chart/$', views.chart, name='chart'),
    url(r'^algo_list/(?P<business>\d{1})/(?P<fromdate>\d{4}\-\d{2}\-\d{2})/(?P<todate>\d{4}\-\d{2}\-\d{2})/$', views.algo_list, name='algo_list'),
    url(r'^query_category/(?P<business>\d{1})/(?P<fromdate>\d{4}\-\d{2}\-\d{2})/(?P<todate>\d{4}\-\d{2}\-\d{2})/$', views.query_category, name='query_category'),
)
