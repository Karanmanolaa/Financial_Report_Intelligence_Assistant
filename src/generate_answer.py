from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from src.retriever import get_retriever


load_dotenv()


# Prepare retrieved chunks into one context block for the LLM.
def format_docs(docs):
    context = ""

    for doc in docs:
        company = doc.metadata.get("company", "unknown")
        year = doc.metadata.get("year", "unknown")
        page = doc.metadata.get("page", "unknown")
        source = doc.metadata.get("source", "unknown")

        context += f"Source: {source}, Company: {company}, Year: {year}, Page: {page}\n"
        context += doc.page_content
        context += "\n\n"

    return context


# Retrieving relevant report chunks and to generate the final answer.
def answer_question(question, company="all", year="all"):
    retriever = get_retriever(company=company, year=year)

    docs = retriever.invoke(question)

    context = format_docs(docs)

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a financial report analyst. "
                "Use only the provided report context to answer the question. "
                "If the answer is not available in the context, say you could not find it in the reports. "
                "Include the source document and page number in the answer."
            ),
            (
                "human",
                "Context:\n{context}\n\nQuestion:\n{question}"
            )
        ]
    )

    model = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    chain = prompt | model | StrOutputParser()

    answer = chain.invoke(
        {
            "context": context,
            "question": question
        }
    )

    return answer


# Quick test for running this file directly.
if __name__ == "__main__":
    question = "What does Microsoft say about AI?"

    answer = answer_question(
        question=question,
        company="microsoft",
        year="2025"
    )

    print(answer)