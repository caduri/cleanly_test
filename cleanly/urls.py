from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.ProductList.as_view(), name='index'),
    # ex: /products/1
    url(r'^products/(?P<product_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /products/1/buy
    url(r'^products/(?P<product_id>[0-9]+)/buy$', views.buy, name='buy'),
    # ex: /products/1/thank_you
    url(r'^products/(?P<product_id>[0-9]+)/thank_you$', views.thank_you, name='thank_you'),
    # ex: /login
    url(r'^login/$', views.login, name='login'),
    # ex: /my_account
    url(r'^my_account/$', views.my_account, name='my_account'),
]
