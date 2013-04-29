from django.conf.urls import patterns, include, url

from views import main, demo, demo2

urlpatterns = patterns('',

    url(r'^$', demo , name = "demo"),
    url(r'^demo2$', demo2 , name = "demo2"),

)