from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'foiaface.views.home', name='home'),
    url(r'^letter/(?P<jurisdiction>\d+)/$', 'foiaface.views.letter', name='letter'),
    url(r'^subdivisions/(?P<parent>\d+)/$', 'foiaface.views.subdivisions', name='subdivisions'),
    url(r'^admin/', include(admin.site.urls)),
)
