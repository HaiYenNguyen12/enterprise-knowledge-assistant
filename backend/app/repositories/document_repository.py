from backend.app.core.db import get_db_connection


class DocumentRepository:
    def __init__(self):
        pass

    def create_document(self, document_id, file_name, file_path, file_size, created_at):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO documents (document_id, file_name, file_path, file_size, created_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (document_id, file_name, file_path, file_size, created_at)
        )
        conn.commit()
        conn.close()

    def get_documents(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM documents")
        documents = cursor.fetchall()
        conn.close()
        return documents
    
    def get_document_by_id(self,document_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM documents where document_id = ?",(document_id,))
        document = cursor.fetchone()
        conn.close()
        return document
    
    def delete_document(self, document_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM documents WHERE document_id = ?", (document_id,))
        conn.commit()
        conn.close()
   