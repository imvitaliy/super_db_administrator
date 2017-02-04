

from django.conf.urls import url
from .api import *

urlpatterns = [
    url(r'^connections/$', ConnectionView.as_view(), name="connections"),
    url(r'^connections/(?P<project>\w+)/$', TablesView.as_view(), name="postgres"),
    url(r'^connections/(?P<project>\w+)/(?P<table>\w+)/fields/$', FieldsView.as_view(), name="columns"),
    # url(r'^connections/(?P<project>\w+)/(?P<table>\w+)/data/(?P<query>.+)/$', FieldsColumnsView.as_view(), name="fields_columns"),
    url(r'^connections/(?P<project>\w+)/(?P<table>\w+)/data/$', FieldsColumnsView.as_view(), name="fields_columns"),

]
