from django.conf.urls import patterns, include, url
from urlcrop import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'urlutils.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.homepage, name='homepage'),
    url(r'(?P<url_hash>[a-zA-Z0-9]{5})', views.handle_redirect)
#    url(r'^admin/', include(admin.site.urls)),
)
