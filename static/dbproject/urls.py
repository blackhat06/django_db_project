from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('', 
    # Examples:
    url(r'^$', 'signups.views.home', name='home'),
    url(r'^thank-you/$', 'signups.views.thankyou', name='thankyou'),
    url(r'^about/$', 'signups.views.about', name='about'),
    url(r'^my_view/$', 'signups.views.my_view', name='my_view'),
    url(r'^welcome/$', 'signups.views.welcome', name='welcome'),
    url(r'^failed/$', 'signups.views.failed', name='failed'),

  
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )
    
    

    
