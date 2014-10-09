from django.conf.urls import patterns, url

from deals import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<deal_id>[0-9]+)/vote/$', views.vote, name='vote'),
)