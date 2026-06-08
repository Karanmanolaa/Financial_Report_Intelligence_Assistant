import re


# Clean one piece of extracted PDF text.
def clean_text(text):
    text = text.replace("\t", " ")

    text = re.sub(r"\s+", " ", text)

    text = text.strip()

    return text


# Clean all loaded document pages and remove empty ones.
def clean_documents(documents):
    cleaned_documents = []

    for document in documents:
        cleaned_text = clean_text(document.page_content)

        if cleaned_text:
            document.page_content = cleaned_text
            cleaned_documents.append(document)

    return cleaned_documents