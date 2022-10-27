import os

import dataset

_db_url = os.environ["DATABASE_URL"]

_connection_url = (
    _db_url.replace("postgres://", "postgresql://", 1)
    if _db_url.startswith("postgres:")
    else _db_url
)

connection = dataset.connect(_connection_url)


def connect():
    return dataset.connect(_connection_url)
