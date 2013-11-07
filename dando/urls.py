from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'main.views.home', name='home'),
    url(r'^ingreso/$',  login, name='login'),
    url(r'^logout/$', logout, {'next_page':'/'}, name='logout'),
    url(r'^registro/$', 'main.views.nuevo_usuario', name='registro'),

    # url(r'^$', 'dando.views.home', name='home'),
    # url(r'^dando/', include('dando.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
