from django.conf.urls import patterns, include, url
from django.contrib import admin
#from myrango import views

urlpatterns = patterns('',
    # Examples:
    url(r'^myrango/', include('myrango.urls')),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
