from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

class Settings(BaseSettings):
  database_name: str
  collection_name: str
  openai_api_key: str
  upload_folder: str
  qdrant_host: str
  qdrant_port: int
  embedding_dimension: int
  embedding_model: str
  model_config = SettingsConfigDict(
    env_file=".env"
  )

settings = Settings()
print("Settings loaded")
print(settings.qdrant_port)
print(type(settings.qdrant_port))
