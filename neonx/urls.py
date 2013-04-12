from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # url(r'^$', 'neonx.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('ad.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
urlpatterns += staticfiles_urlpatterns()