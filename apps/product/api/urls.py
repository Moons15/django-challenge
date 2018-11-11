from django.conf.urls import url
from apps.product.api.views import ListProductAPIView, CreateProductAPIView, \
    GetUpdateDeleteProductAPIView, PutProductAPIView

app_name = 'account'
urlpatterns = [
    url(r'^list/$', ListProductAPIView.as_view()),
    url(r'^create/$', CreateProductAPIView.as_view()),
    url(r'^(?P<pk>\d+)/$', GetUpdateDeleteProductAPIView.as_view()),
    url(r'^(?P<pk>\d+)/put/$', PutProductAPIView.as_view({'put': 'update'})),
]
