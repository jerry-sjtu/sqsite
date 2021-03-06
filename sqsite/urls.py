from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sqsite.views.home', name='home'),
    # url(r'^sqsite/', include('sqsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('homepage.urls', namespace='homepage')),
    url(r'^kpi/', include('kpi.urls', namespace='kpi')),
    url(r'^hotquery/', include('hotquery.urls', namespace='hotquery')),
    url(r'^cheatquery/', include('cheatquery.urls', namespace='cheatquery')),
)
