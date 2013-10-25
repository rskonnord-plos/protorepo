from django.conf.urls import patterns, url

from api import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^read/(?P<item_name>.*)', views.read, name='read'),
)
