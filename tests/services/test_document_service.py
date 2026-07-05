import pytest
from  backend.app.services.document_service import DocumentService 
from backend.app.models.document import DocumentResponse

# class FakeDocumentRepository:
#   def get_documents(self, offset: int, limit: int, keyword: str | None = None , sort_by: str | None = None, sort_order: str | None = None):
#     return (
#       [
#         {
#           "document_id": "1",
#           "file_name": "test_document.pdf",
#           # "file_path": "/path/to/test_document.pdf",
#           "file_size": 1024,
#           "created_at": "2023-01-01 00:00:00"
#         }
#       ],
#       1
#     )

# class FakeQdrantRepository:
#   pass

def test_get_documents_should_return_document_list(mocker):
  document_repository_mock = mocker.Mock()
  document_repository_mock.get_documents.return_value = (
    [
      {
        "document_id": "1",
        "file_name": "test_document.pdf",
        # "file_path": "/path/to/test_document.pdf",
        "file_size": 1024,
        "created_at": "2023-01-01 00:00:00"
      }
    ],
    1
  )
  
  qdrant_repository_mock = mocker.Mock()
  service = DocumentService(document_repository_mock, qdrant_repository_mock)
  documents, total_items = service.get_documents(page=1, page_size=10, keyword=None, sort_by="created_at", sort_order="desc")
  document_repository_mock.get_documents.assert_called_once_with(offset=0, limit=10, keyword=None, sort_by="created_at", sort_order="desc")
  assert total_items == 1
  assert len(documents) == 1
  assert isinstance(documents[0], DocumentResponse)
  assert documents[0].document_id == "1"
  assert documents[0].file_name == "test_document.pdf"
  # assert documents[0].file_path == "/path/to/test_document.pdf"
  assert documents[0].file_size == 1024
  assert documents[0].created_at == "2023-01-01 00:00:00"


def test_get_documents_should_return_empty_list(mocker):
  document_repository_mock = mocker.Mock()
  document_repository_mock.get_documents.return_value = ([], 0)
  
  qdrant_repository_mock = mocker.Mock()
  service = DocumentService(document_repository_mock, qdrant_repository_mock)
  documents, total_items = service.get_documents(page=1, page_size=10, keyword=None, sort_by="created_at", sort_order="desc")
  assert total_items == 0
  assert documents == []


def test_get_documents_should_raise_exception_when_repository_fails(mocker):
    document_repository = mocker.Mock()
    qdrant_repository = mocker.Mock()

    document_repository.get_documents.side_effect = Exception("Database Error")

    service = DocumentService(
        document_repository=document_repository,
        qdrant_repository=qdrant_repository
    )

    with pytest.raises(Exception, match="Database Error"):
        service.get_documents(
            page=1,
            page_size=10
        )