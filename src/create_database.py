from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

from src.chunk_documents import chunk_documents
from src.config import VECTORSTORE_DIR, COLLECTION_NAME


load_dotenv()

# Create the ChromaDB vector database from the annual report chunks.
def build_vectorstore():
    chunks = chunk_documents()

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small",
        chunk_size=3,
        max_retries=10,
        retry_min_seconds=5,
        retry_max_seconds=20
)

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(VECTORSTORE_DIR),
        collection_name=COLLECTION_NAME
    )

    return vectorstore



# Running this file directly to create and check the vector database.
if __name__ == "__main__":
    vectorstore = build_vectorstore()

    print("Vector store created successfully.")
    print(f"Total chunks stored: {vectorstore._collection.count()}")