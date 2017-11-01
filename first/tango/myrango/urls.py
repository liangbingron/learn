from django.conf.urls import patterns,url
from myrango import views
from django.conf import settings



urlpatterns=patterns('',
	url(r'about/$',views.about,name='about'),
	url(r'^$',views.index,name='index'),
   url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
)
#if not settings.DEBUG:
 #       urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
print "using static folder"


