from django.conf.urls import patterns, url
from adam import views

urlpatterns = patterns('',
    url(r'^$', views.main, name="main")
)
