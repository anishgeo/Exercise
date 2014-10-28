from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from tasklist import views

urlpatterns = patterns('',
    
    url(r'^$', views.index, name='index'),
    
    url(r'^register/$', views.register, name='register'),
)
