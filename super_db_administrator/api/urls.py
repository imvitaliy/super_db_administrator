

from django.conf.urls import url
from .api import *

urlpatterns = [
    url(r'^connections/$', ConnectionView.as_view(), name="connections"),
    url(r'^connections/postgres/$', PostgresTablesView.as_view(), name="postgres"),
    url(r'^connections/postgres/(?P<table>\w+)/$', PostgresTableColumnsView.as_view(), name="columns"),

]
