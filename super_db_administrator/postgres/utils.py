import psycopg2
import itertools

from django.core.paginator import Paginator
from api.models import ConnectionDb
from api.serializers import ConnectionSerializer


def get_all_connections_data():
    try:
        connection = ConnectionDb.objects.all()
        serializer = ConnectionSerializer(connection, many=True)
        serializer = serializer.data
        return serializer
    except Exception as e:
        print (e)

def get_serializer_data(project):
    try:
        connection = ConnectionDb.objects.get(name=project)
        serializer = ConnectionSerializer(connection)
        serializer = serializer.data
        return serializer
    except Exception as e:
        print(e)


def get_connections_credentials(serializer):
    psycopg_connection = "dbname={} user={} password={} host={}".format(
                        serializer['db_name'],
                        serializer['username'],
                        serializer['password'],
                        serializer['host'])

    return psycopg_connection

def get_postgres_tables(serializer):
    conn = psycopg2.connect(get_connections_credentials(serializer))
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

    return {"tables": list_tables}

def get_postgres_fields(serializer, table):
    conn = psycopg2.connect(get_connections_credentials(serializer))
    cur = conn.cursor()
    query = """
                SELECT column_name
                FROM information_schema.columns
                WHERE table_schema = 'public'
                AND table_name = '{}';
            """
    cur.execute(query.format(table))
    fields = cur.fetchall()
    list_fields = list(itertools.chain.from_iterable(fields))
    cur.close()
    conn.close()

    return {"fields": list_fields}

def get_postgres_columns(serializer, table):
    conn = psycopg2.connect(get_connections_credentials(serializer))
    cur = conn.cursor()
    query_param = "*"
    query = """
                SELECT {} FROM {};
            """
    cur.execute(query.format(query_param, table))
    fields = cur.fetchall()
    list_columns = list(itertools.chain.from_iterable(fields))
    cur.close()
    conn.close()
    paginate_list = Paginator(list_columns,10)
    page = paginate_list.page(100)
    return {"columns": page.object_list}
