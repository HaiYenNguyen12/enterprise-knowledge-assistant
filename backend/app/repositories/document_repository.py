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

    def get_documents(self, offset: int, limit: int, keyword: str | None = None , sort_by: str | None = None, sort_order: str | None = None):

        allowed_sort_fields = {"document_id", "file_name", "file_size", "created_at"}
        if sort_by not in allowed_sort_fields:
            sort_by = "created_at"  # Default to created_at if invalid field is provided    
        
        sort_order = sort_order.lower()
        if sort_order not in ["asc", "desc"]:
            sort_order = (sort_order or "desc").lower()  # Default to descending if invalid order is provided
            
        conn = get_db_connection()
        cursor = conn.cursor()

        if keyword:
            total_items = cursor.execute("SELECT COUNT(*) FROM documents WHERE file_name LIKE ?", (f"%{keyword}%",)).fetchone()[0]
            cursor.execute(f"SELECT * FROM documents WHERE file_name LIKE ? ORDER BY {sort_by} {sort_order} LIMIT ? OFFSET ?", (f"%{keyword}%", limit, offset))
        else:
            total_items = cursor.execute("SELECT COUNT(*) FROM documents").fetchone()[0]
            cursor.execute(f"SELECT * FROM documents ORDER BY {sort_by} {sort_order} LIMIT ? OFFSET ?", (limit, offset))
        documents = cursor.fetchall()
        conn.close()
        return documents, total_items

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
   