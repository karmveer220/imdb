from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^movies/', include('movies.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
