from django.conf.urls import patterns, include, url

from views import main

urlpatterns = patterns('',

    url(r'^$', main , name = "main"),

)