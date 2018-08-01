from django.conf.urls import url, include
from . import views



urlpatterns = [


    url(r'^$', views.PdfView.as_view(), name = 'ebook'),
    url(r'^(?P<pk>\d+)/$', views.EbookDetail.as_view(), name='ebookdetail'),
    url(r'^sellebook/$', views.sellebooks, name = 'sellebook'),


]

