from django.conf.urls import patterns, include, url
from django.contrib import admin
from agenda.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('agenda.views',
    # Examples:
    # url(r'^$', 'challenge.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'home', name='home'),
	url(r'^signin/$', Create.as_view(), name='signin'),
	url(r'^update/(?P<pk>[0-9]+)/$', Update.as_view(), name='update'),
	url(r'^list/$', List.as_view(), name='list'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^delete/(?P<pk>[0-9]+)/$', Delete.as_view(), name='delete'),
)
