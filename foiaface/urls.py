from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'foiaface.views.home', name='home'),
     url(r'^subdivisions/(?P<j_id>\d+)/$', 'foiaface.views.subdivisions', name='subdivisions'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
