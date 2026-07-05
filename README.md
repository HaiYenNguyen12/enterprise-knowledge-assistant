
````markdown
# Enterprise Knowledge Assistant

An AI-powered enterprise knowledge assistant that enables users to upload PDF documents, retrieve relevant information, and ask natural language questions using Retrieval-Augmented Generation (RAG) and Large Language Models (LLMs).

The application also provides document management capabilities, including document uploading, searching, sorting, and pagination. It is built using a layered backend architecture with FastAPI, Repository Pattern, Dependency Injection, SQLite, and Qdrant Vector Database.

---

## ✨ Features

### AI Features

- Upload PDF documents
- Extract text from PDF files
- Split documents into semantic chunks
- Generate vector embeddings
- Store embeddings in Qdrant
- Retrieve relevant document chunks
- Answer questions using Retrieval-Augmented Generation (RAG)

### Document Management

- Upload documents
- Delete documents
- Search documents by filename
- Pagination
- Sorting
- Metadata support

### Backend Features

- Layered Architecture
- Repository Pattern
- Dependency Injection
- Global Exception Handling
- Logging
- Environment Configuration (.env)
- Standardized API Response
- Swagger Documentation

---

# 🛠 Tech Stack

## Backend

- Python 3.13
- FastAPI

## AI / Machine Learning

- Retrieval-Augmented Generation (RAG)
- Sentence Transformers
- BAAI/bge-small-en-v1.5

## Vector Database

- Qdrant

## Database

- SQLite

## Libraries

- Pydantic
- Pydantic Settings
- PyMuPDF
- Uvicorn

## API Documentation

- Swagger UI (OpenAPI)

---

# 🏗 Architecture

```
                    +----------------------+
                    |      FastAPI API     |
                    +----------+-----------+
                               |
                               v
                      +------------------+
                      |      Router      |
                      +--------+---------+
                               |
                               v
                      +------------------+
                      |  DocumentService |
                      +--------+---------+
                               |
               +---------------+---------------+
               |                               |
               v                               v
     +---------------------+        +----------------------+
     | DocumentRepository  |        |  QdrantRepository    |
     +----------+----------+        +----------+-----------+
                |                              |
                v                              v
          SQLite Database              Qdrant Vector DB
```

---

# 📂 Project Structure

```
backend/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── exceptions/
│   ├── models/
│   ├── repositories/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── uploads/
│
└── requirements.txt
```

---

# 🚀 Installation

## Clone repository

```bash
git clone https://github.com/<your-github>/enterprise-knowledge-assistant.git

cd enterprise-knowledge-assistant
```

## Create virtual environment

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Mac/Linux

```bash
source .venv/bin/activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Configure environment variables

Create `.env`

```env
DATABASE_NAME=backend/app/database/knowledge.db

UPLOAD_FOLDER=uploads

QDRANT_HOST=localhost
QDRANT_PORT=6333
COLLECTION_NAME=knowledge_base

EMBEDDING_MODEL=BAAI/bge-small-en-v1.5
EMBEDDING_DIMENSION=384
```

## Start Qdrant

```bash
docker run -p 6333:6333 qdrant/qdrant
```

## Run application

```bash
uvicorn backend.app.main:app --reload
```

Swagger

```
http://localhost:8000/docs
```

---

# 📌 API Endpoints

## Documents

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/documents/upload` | Upload PDF document |
| GET | `/documents` | Get documents with pagination, search and sorting |
| DELETE | `/documents/{document_id}` | Delete document |

---

## RAG

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/ask` | Ask questions using uploaded documents |

---

# Example API

## Upload Document

```
POST /documents/upload
```

## Ask Question

```
POST /ask
```

```json
{
    "question":"What is the insurance policy?",
    "document_ids":[
        "...",
        "..."
    ]
}
```

## Search Documents

```
GET /documents?keyword=insurance
```

## Pagination

```
GET /documents?page=2&page_size=10
```

## Sorting

```
GET /documents?sort_by=file_name&sort_order=asc
```

---

# 📖 Design Patterns

- Repository Pattern
- Service Layer
- Dependency Injection
- Layered Architecture

# 👩‍💻 Author

**Nguyen Thi Hai Yen**

AI Engineer