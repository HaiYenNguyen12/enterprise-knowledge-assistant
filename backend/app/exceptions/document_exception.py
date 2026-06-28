class DocumentException(Exception):
  pass


class DocumentNotFoundException(DocumentException):
  def __init__(self, document_id: str):
    super().__init__(f"Document {document_id} not found")
