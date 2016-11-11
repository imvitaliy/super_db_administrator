import os
import psycopg2
import itertools

from django.http import JsonResponse
from django.views.generic import View

from api.models import ConnectionDb
from api.serializers import ConnectionSerializer


class ConnectionView(View):
    http_method_names = ['get']

    def get(self, request):
        try:
            connection = ConnectionDb.objects.all()
            serializer = ConnectionSerializer(connection, many=True)

            return JsonResponse(serializer.data, safe=False)
        except Exception as e:
            print (e)


class PostgresTablesView(View):
    http_method_names = ['get']

    def get(self, request):
        try:
            connection = ConnectionDb.objects.all()
            serializer = ConnectionSerializer(connection, many=True)
            serializer = serializer.data[0]
            conn = psycopg2.connect(dbname=serializer['db_name'],
                                    user=serializer['username'],
                                    password=serializer['password'],
                                    host=serializer['host'])
            cur = conn.cursor()
            query = """
                            SELECT
                             tablename
                            FROM
                             pg_catalog.pg_tables
                            WHERE
                             schemaname != 'pg_catalog'
                            AND schemaname != 'information_schema';
                        """
            cur.execute(query)
            tables = cur.fetchall()
            list_tables = list(itertools.chain.from_iterable(tables))
            cur.close()
            conn.close()

            return JsonResponse({"tables":list_tables})
        except Exception as e:
            print (e)


class PostgresTableColumnsView(View):
    http_method_names = ['get']

    def get(self, request, table):
        try:
            connection = ConnectionDb.objects.all()
            serializer = ConnectionSerializer(connection, many=True)
            serializer = serializer.data[0]
            conn = psycopg2.connect(dbname=serializer['db_name'],
                                    user=serializer['username'],
                                    password=serializer['password'],
                                    host=serializer['host'])
            cur = conn.cursor()
            query = """
                        SELECT column_name
                        FROM information_schema.columns
                        WHERE table_schema='public'
                        AND table_name='{}';
                    """
            cur.execute(query.format(table))
            fields = cur.fetchall()
            list_fields = list(itertools.chain.from_iterable(fields))
            cur.close()
            conn.close()

            return JsonResponse({"fields":list_fields})
        except Exception as e:
            print (e)
