import os

import psycopg

from psycopg.rows import dict_row

_db_url = os.environ["DATABASE_URL"]


def pg_connect(autocommit=True):
    return psycopg.connect(_db_url, row_factory=dict_row, autocommit=autocommit)


def format_placeholders(statement, column_names):
    def by_type(bind_type, names):
        return psycopg.sql.SQL(", ").join(map(bind_type, names))

    return psycopg.sql.SQL(statement).format(
        by_type(psycopg.sql.Identifier, column_names),
        by_type(psycopg.sql.Placeholder, column_names),
    )


def execute_statement(statement, params):
    with pg_connect() as connection:
        with connection.cursor() as cursor:
            with connection.transaction():
                cursor.execute(statement, params)
