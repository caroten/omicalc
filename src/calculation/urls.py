from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'calculation.views',
    url(r'^$', 'index'),
)
