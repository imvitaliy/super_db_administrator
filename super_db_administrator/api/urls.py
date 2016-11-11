

from django.conf.urls import url
from .api import *

urlpatterns = [
    url(r'^connections/$', ConnectionView.as_view(), name="connections"),
    url(r'^connections/(?P<project>\w+)/$', TablesView.as_view(), name="postgres"),
    url(r'^connections/(?P<project>\w+)/(?P<table>\w+)/$', FieldsView.as_view(), name="columns"),

]
