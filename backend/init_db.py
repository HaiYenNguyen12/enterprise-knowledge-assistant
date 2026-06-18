from app.core.db import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()

cursor.execute(
  """
  CREATE TABLE IF NOT EXISTS documents (
  document_id TEXT PRIMARY KEY,
  file_name TEXT NOT NULL,
  file_path TEXT NOT NULL, 
  file_size INTEGER NOT NULL,
  created_at TEXT NOT NULL
  )
"""
)
conn.commit()
conn.close()

print("The database is created sucessfully")