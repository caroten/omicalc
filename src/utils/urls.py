from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
)

# urlpatterns = patterns(
#     '',
#     url(r'^$', include(urls, app_name='app')),
# )
