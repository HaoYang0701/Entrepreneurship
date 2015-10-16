from django.conf.urls import include, url
from django.contrib import admin
from website import views

urlpatterns = [
    url(r'^website/', include('website.urls')),
    url(r'^$', 'website.views.home'),

]
