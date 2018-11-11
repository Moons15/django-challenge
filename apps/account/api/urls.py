from django.conf.urls import url
from apps.account.api.views import CreateSuperUserAPIView, LoginAPIView

app_name = 'account'
urlpatterns = [
    url(r'^register/$', CreateSuperUserAPIView.as_view()),
    url(r'^login/$', LoginAPIView.as_view()),
]
