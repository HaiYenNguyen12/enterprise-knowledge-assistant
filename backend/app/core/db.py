import sqlite3

DATABASE_NAME = "backend/app/database/knowledge.db"

def get_db_connection():
    return sqlite3.connect(DATABASE_NAME)
