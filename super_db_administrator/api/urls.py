

from django.conf.urls import url

from .views import user_api_view, user_detail_api_view

urlpatterns = [
    url(r'^users/$', user_api_view),
    url(r'^users/(?P<user>[0-9]{1})/$', user_detail_api_view),
]
