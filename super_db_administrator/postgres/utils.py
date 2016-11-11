import psycopg2
import itertools

def get_postgres_tables(serializer):
    conn = psycopg2.connect(dbname = serializer['db_name'],
                            user = serializer['username'],
                            password = serializer['password'],
                            host = serializer['host'])
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
    conn = psycopg2.connect(dbname = serializer['db_name'],
                            user = serializer['username'],
                            password = serializer['password'],
                            host = serializer['host'])
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
