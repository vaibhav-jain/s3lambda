from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('apps.api.urls')),  # grappelli URLS
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Change to whatever you like
admin.site.site_title = 's3lambda Administration'
admin.site.index_title = 's3lambda Administration'
admin.site.site_header = 's3lambda Administration'
