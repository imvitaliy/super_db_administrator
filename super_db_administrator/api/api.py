import os
import psycopg2

from django.http import JsonResponse
from django.views.generic import View

from api.models import ConnectionDb
from api.serializers import ConnectionSerializer

class ConnectionView(View):
    http_method_names = ['get']

    def get(self, request):
        connection = ConnectionDb.objects.all()
        serializer = ConnectionSerializer(connection, many=True)
        return JsonResponse(serializer.data, safe=False)


class PostgresTablesView(View):
    http_method_names = ['get']
    def get(self, request):
        connection = ConnectionDb.objects.all()
        serializer = ConnectionSerializer(connection, many=True)
        serializer = serializer.data[0]
        conn = psycopg2.connect(dbname=serializer['db_name'],
                                user=serializer['username'],
                                password=serializer['password'],
                                host=serializer['host'])
        cur = conn.cursor()
        tables = cur.execute("""
                                SELECT n.nspname as "Schema",
                                c.relname as "Name",
                                CASE c.relkind WHEN 'r' THEN 'table' WHEN 'v' THEN 'view' WHEN 'i' THEN 'index' WHEN 'S' THEN 'sequence' WHEN 's' THEN 'special' END as "Type",
                                pg_catalog.pg_get_userbyid(c.relowner) as "Owner"
                                FROM pg_catalog.pg_class c
                                    LEFT JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace
                                WHERE c.relkind IN ('r','')
                                    AND n.nspname <> 'pg_catalog'
                                    AND n.nspname <> 'information_schema'
                                    AND n.nspname !~ '^pg_toast'
                                AND pg_catalog.pg_table_is_visible(c.oid)
                                ORDER BY 1,2;
                            """)
        tables = cur.fetchall()

        print(tables)
        cur.close()
        conn.close()
        return JsonResponse(tables, safe=False)


class PostgresTableColumnsView(View):
    http_method_names = ['get']

    def get(self, request, table):
        try:
            # table_name = request.GET.get('table_name')
            print(table)
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
            tables = cur.execute(query.format(table))

            tables = cur.fetchall()
            print(tables)
            cur.close()
            conn.close()
            return JsonResponse(tables, safe=False)
        except Exception as e:
            print (e)
