from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'krokodeal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^deals/', include('deals.urls', namespace="deals", app_name="deals")),
    url(r'^deals/', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',include('deals.urls', namespace="deals")),
)
