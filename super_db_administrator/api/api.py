import os
import psycopg2
import itertools

from django.http import JsonResponse
from django.views.generic import View

from api.models import ConnectionDb
from api.serializers import ConnectionSerializer
from postgres.utils import *

class ConnectionView(View):
    http_method_names = ['get']

    def get(self, request):
        try:
            connection = ConnectionDb.objects.all()
            serializer = ConnectionSerializer(connection, many=True)

            return JsonResponse(serializer.data, safe=False)
        except Exception as e:
            print (e)


class TablesView(View):
    http_method_names = ['get']

    def get(self, request, project):
        try:
            connection = ConnectionDb.objects.get(project_name=project)
            print(connection)
            serializer = ConnectionSerializer(connection)
            serializer = serializer.data

            result = get_postgres_tables(serializer)

            return JsonResponse(result)
        except Exception as e:
            print (e)


class FieldsView(View):
    http_method_names = ['get']

    def get(self, request, project, table):
        try:
            connection = ConnectionDb.objects.get(project_name=project)
            serializer = ConnectionSerializer(connection)
            serializer = serializer.data

            result = get_postgres_fields(serializer, table)

            return JsonResponse(result)
        except Exception as e:
            print (e)
