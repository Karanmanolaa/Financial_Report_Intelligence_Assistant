# Financial AI Assistant

This is a RAG project I built to search and answer questions from company annual reports.

I used Microsoft and NVIDIA annual reports because both companies are closely connected to AI, cloud, GPUs, and data center growth. The idea was to build something more useful than a normal PDF chatbot, where the app can search stored reports and answer questions using only the relevant report content.

## What this project does

The app lets the user choose a company and year, then ask a question about the annual report.

Example questions:

text What does Microsoft say about AI? What are Microsoft's main business risks? What does NVIDIA say about data center growth? What are NVIDIA's main business risks? 

The app retrieves the most relevant chunks from the reports and sends only those chunks to the LLM. This keeps the answer more grounded and avoids sending the full PDF every time.

## Reports used

The current version uses:

text Microsoft Annual Report 2024 Microsoft Annual Report 2025 NVIDIA Annual Report 2024 NVIDIA Annual Report 2025 

## How it works

The project follows this flow:

text PDF reports → load pages → clean text → split into chunks → create embeddings → store in ChromaDB → retrieve relevant chunks → generate answer with GPT-4o-mini 

## Tech stack

text Python Streamlit LangChain ChromaDB OpenAI API PyMuPDF python-dotenv 

## Main files

text app.py                  Streamlit app load_documents.py       loads PDF pages preprocess_text.py      cleans extracted text chunk_documents.py      splits text into chunks create_database.py      creates the ChromaDB vector database retriever.py            searches relevant chunks generate_answer.py      generates the final answer config.py               stores folder paths and collection name 

## How to run

Create a virtual environment:

bash python3 -m venv venv source venv/bin/activate 

Install dependencies:

bash pip install -r requirements.txt 

Create a .env file:

text OPENAI_API_KEY=your_api_key_here 

Create the vector database:

bash python -m src.create_database 

Run the app:

bash streamlit run app.py 

## Current version

This is the first working version of the project.

It can answer questions from the stored reports and supports company/year filtering. It works best for questions about AI strategy, risks, data centers, cloud, and business discussion.

It is not yet a full financial calculation engine. For questions like profit margin comparison or revenue growth, I would add a separate structured financial metrics file later.
