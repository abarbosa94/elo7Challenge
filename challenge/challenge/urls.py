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
	url(r'^list/$', List.as_view(), name='list'),
    url(r'^admin/', include(admin.site.urls)),
)
