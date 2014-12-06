from django.conf.urls import patterns, url

from deals import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^add/$', views.addDeal, name='add'), 
    #url(r'^login/$', views.loginView, name='login'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', views.logoutView, name='logout'), 
    url(r'^(?P<deal_id>[0-9]+)/vote/$', views.vote, name='vote'),
    
    
#(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'myapp/login.html'},{'template_name': 'myapp/login.html'}),
    
)