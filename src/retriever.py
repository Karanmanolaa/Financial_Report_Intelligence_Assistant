from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

from src.config import VECTORSTORE_DIR, COLLECTION_NAME


load_dotenv()


# Connect to ChromaDB and create a retriever with optional company/year filters.
def get_retriever(company="all", year="all"):
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

    vectorstore = Chroma(
        persist_directory=str(VECTORSTORE_DIR),
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings
    )

    conditions = []

    if company != "all":
        conditions.append({"company": company})

    if year != "all":
        conditions.append({"year": year})

    if len(conditions) == 1:
        filters = conditions[0]

    elif len(conditions) > 1:
        filters = {"$and": conditions}

    else:
        filters = {}

    search_kwargs = {"k": 5}

    if filters:
        search_kwargs["filter"] = filters

    retriever = vectorstore.as_retriever(
        search_kwargs=search_kwargs
    )

    return retriever


# Quick test to check whether retrieval works for a selected company and year.
if __name__ == "__main__":
    retriever = get_retriever(
        company="microsoft",
        year="2024"
    )

    question = "What does Microsoft say about AI?"

    docs = retriever.invoke(question)

    print(f"Retrieved chunks: {len(docs)}")
    print()

    for doc in docs:
        print(doc.metadata)
        print(doc.page_content[:500])
        print()