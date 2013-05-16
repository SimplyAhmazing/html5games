from django.conf.urls import patterns, include, url

from views import * #main, api, api2, api3, api4, main2

urlpatterns = patterns('',

	url(r'^api.json$', api),
	url(r'^api2/$', api2),
	url(r'^api3$', api3),
	url(r'^api4.json$', api4),
	url(r'^(?P<qry>\w+).json$', headings_api),
    url(r'^$', main, name = "main"),
    url(r'^demo2$', main2, name = "main"),
    url(r'^demo3$', main3, name = "main"),
)