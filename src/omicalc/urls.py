from django.conf.urls import patterns, include, url
from django.contrib import admin
import utils

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'omicalc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^utils/', include(utils.site.urls)),
    url(r'^calculation/', include('calculation.urls')),
)
