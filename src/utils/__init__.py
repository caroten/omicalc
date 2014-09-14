from .urls import urlpatterns

class Site:
    @property
    def urls(self):
        return urlpatterns, 'utils', 'utils'

site = Site()
