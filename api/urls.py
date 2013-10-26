from django.conf.urls import patterns, url

from api import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^item/(?P<item_name>.*)', views.item, name='item'),
)
