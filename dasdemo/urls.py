from django.conf.urls import patterns, include, url

from views import main, demo

urlpatterns = patterns('',

    url(r'^$', demo , name = "demo"),

)