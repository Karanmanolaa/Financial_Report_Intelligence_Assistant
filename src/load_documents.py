from langchain_community.document_loaders import PyMuPDFLoader

from src.config import DATA_DIR


# Load all PDF reports from the data folder and attach basic metadata.
def load_pdf_documents():
    documents = []

    pdf_files = list(DATA_DIR.glob("*.pdf"))

    for pdf_file in pdf_files:
        file_name = pdf_file.name
        company = file_name.split("_")[0]
        year = file_name.split("_")[1].replace(".pdf", "")

        loader = PyMuPDFLoader(str(pdf_file))
        pages = loader.load()

        for page in pages:
            page.metadata["company"] = company
            page.metadata["year"] = year
            page.metadata["source"] = file_name

            documents.append(page)

    return documents


# Quick test to check that the PDFs are loading correctly.
if __name__ == "__main__":
    docs = load_pdf_documents()

    print(f"Total pages loaded: {len(docs)}")

    print(docs[0].metadata)

    print(docs[0].page_content[:500])