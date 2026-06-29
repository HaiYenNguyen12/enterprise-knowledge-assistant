import sqlite3
from backend.app.core.settings import settings

# DATABASE_NAME = settings.database_name

def get_db_connection():
    conn = sqlite3.connect(settings.database_name)
    conn.row_factory = sqlite3.Row
    return conn
