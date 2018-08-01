from django.conf.urls import url, include
from . import views



urlpatterns = [

    url(r'^login/$', views.Facebook.as_view(), name = 'facebook'),
    url(r'^detail/$', views.DetailView, name = 'detail'),
    url(r'^$', views.buy.as_view(), name = 'buy'),
    url(r'^sell/$', views.sell, name = 'sell'),
    url(r'^(?P<pk>\d+)/$', views.BookDetail.as_view(), name='bookdetail'),
    url(r'^user/$', views.UserCreate, name = 'user'),
    url(r'^detail/$', views.DetailView, name = 'detail'),



]

