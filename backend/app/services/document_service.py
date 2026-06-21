from backend.app.repositories.document_repository import DocumentRepository


class DocumentService:
    def __init__(self, document_repository):
        self.document_repository = document_repository

    def upload_document(self, file):
        return self.document_repository.create(file)

    def get_documents(self):
        pass

    def update_document(self, document_id, document_data):
        return self.document_repository.update(document_id, document_data)

    def delete_document(self, document_id):
        return self.document_repository.delete(document_id)