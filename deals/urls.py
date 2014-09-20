from django.conf.urls import patterns, url

from deals import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)