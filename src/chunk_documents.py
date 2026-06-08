from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.load_documents import load_pdf_documents
from src.preprocess_text import clean_documents


# lets chunk the cleaned annual report pages into smaller pieces for retrieval.
def chunk_documents():
    documents = load_pdf_documents()

    cleaned_documents = clean_documents(documents)

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150
    )

    chunks = text_splitter.split_documents(cleaned_documents)

    return chunks

# lets now test to check how many chunks were created and inspect the first chunk.
if __name__ == "__main__":
    chunks = chunk_documents()

    print(f"Total chunks created: {len(chunks)}")
    print(chunks[0].metadata)
    print(chunks[0].page_content[:500])