from django.conf.urls import patterns, url

from deals import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^add/$', views.addDeal, name='add'), 
    url(r'^register/$', views.registerView, name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^password/reset/$', 'django.contrib.auth.views.password_reset', {'template_name': 'deals/password_reset_form.html'}, name='passwordReset'),
    url(r'^password/reset_done/$', 'django.contrib.auth.views.password_reset_done', {'template_name': 'deals/password_reset_done.html'}, name='password_reset_done'),
    url(r'^logout/$', views.logoutView, name='logout'), 
    url(r'^(?P<deal_id>[0-9]+)/vote/$', views.vote, name='vote'),
    
    
)