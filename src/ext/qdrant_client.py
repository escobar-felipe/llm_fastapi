import os

from langchain_openai import OpenAIEmbeddings
from qdrant_client import QdrantClient

qdrant_client = QdrantClient(
    host=os.environ.get("QDRANT_HOST"),
    api_key=os.environ.get("QDRANT_APIKEY"),
    https=False,
)


embedding_function = OpenAIEmbeddings()
