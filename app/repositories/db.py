import os

import dataset
import psycopg

from psycopg.rows import dict_row

_db_url = os.environ["DATABASE_URL"]

_connection_url = (
    _db_url.replace("postgres://", "postgresql://", 1)
    if _db_url.startswith("postgres:")
    else _db_url
)

connection = dataset.connect(_connection_url)


def connect():
    return dataset.connect(_connection_url)


def pg_connect(autocommit=True):
    return psycopg.connect(_db_url, row_factory=dict_row, autocommit=autocommit)


def format_placeholders(statement, column_names):
    def by_type(bind_type, names):
        return psycopg.sql.SQL(", ").join(map(bind_type, names))

    return psycopg.sql.SQL(statement).format(
        by_type(psycopg.sql.Identifier, column_names),
        by_type(psycopg.sql.Placeholder, column_names),
    )
