from django.conf.urls import include, url
from website import views

urlpatterns = [
   
     url(r'^$', 'website.views.home'),
     url(r'^Agri$', 'website.views.agri',name='Agri'),
     url(r'^Contact$', 'website.views.contact',name='Contact'),
     url(r'^Cust$', 'website.views.cust',name='Cust'),
     url(r'^Oper$', 'website.views.oper',name='Oper'),
     url(r'^Risk$', 'website.views.risk',name='Risk'),
     url(r'^Trans$', 'website.views.trans',name='Trans'),
]