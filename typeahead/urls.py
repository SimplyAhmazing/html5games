from django.conf.urls import patterns, include, url

from views import main, api, api2, api3

urlpatterns = patterns('',

	url(r'^api.json/$', api),
	url(r'^api2.json/$', api2),
	url(r'^api3.json/$', api3),
    url(r'^$', main, name = "main"),
)