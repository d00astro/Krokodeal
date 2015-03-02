from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static

from deals import views, feeds

urlpatterns = patterns('',
    url(r'^$', views.newDealsView.as_view()),
    url(r'^new/$', views.newDealsView.as_view(), name='new'),
    url(r'^new/(?P<page>[0-9]+)/$', views.newDealsView.as_view(), name='newPaged'),
    url(r'^hot/$', views.hotDealsView.as_view(), name='hot'),
    url(r'^detail/(?P<slug>[-\w]+)/$', views.dealDetailView.as_view(), name='dealDetail'),   
    url(r'^add/$', views.addDeal, name='add'),
    url(r'^about/$', views.about.as_view(), name='about'), 
    url(r'^(?P<deal_id>[0-9]+)/vote/$', views.vote, name='vote'),
    
    #Users
    url(r'^register/$', views.registerView, name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^password/reset/$', 'django.contrib.auth.views.password_reset', {'template_name': 'deals/password_reset_form.html'}, name='passwordReset'),
    url(r'^password/reset_done/$', 'django.contrib.auth.views.password_reset_done', {'template_name': 'deals/password_reset_done.html'}, name='password_reset_done'),
    url(r'^logout/$', views.logoutView, name='logout'),
    
    #Footer
    url(r'^disclaimer/$', views.disclaimer.as_view(), name='disclaimer'),
    
    #Feeds
    url(r'^hot/feed/rss$', feeds.HotDealsFeed()),
    
    
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)