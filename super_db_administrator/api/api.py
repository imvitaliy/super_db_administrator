import os
import psycopg2
import itertools

from django.http import JsonResponse
from django.views.generic import View

from postgres.utils import *

class ConnectionView(View):
    http_method_names = ['get']

    def get(self, request):
        connections = get_all_connections_data()

        return JsonResponse(connections, safe=False)


class TablesView(View):
    http_method_names = ['get']

    def get(self, request, project):
        serializer = get_serializer_data(project)
        result = get_postgres_tables(serializer)

        return JsonResponse(result)


class FieldsView(View):
    http_method_names = ['get']

    def get(self, request, project, table):
        serializer = get_serializer_data(project)
        result = get_postgres_fields(serializer, table)

        return JsonResponse(result)


class FieldsColumnsView(View):
    http_method_names = ['get']

    def get(self, request, project, table):

            serializer = get_serializer_data(project)

            # columns = get_postgres_columns(serializer, table, query)
            fields = get_postgres_fields(serializer, table)
            fields_columns = get_postgres_columns(serializer, table)

            return JsonResponse(fields_columns)
