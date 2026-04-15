import streamlit as st
import os
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

load_dotenv()

st.title("🧠 Knowledge Base AI Assistant")

DATA_PATH = "data"
DB_PATH = "vectorstore"

# Load documents
loader = PyPDFDirectoryLoader(DATA_PATH)
documents = loader.load()

# Split documents
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
docs = splitter.split_documents(documents)

# Create embeddings
embedding = OpenAIEmbeddings()

# Create vector database
db = Chroma.from_documents(
    docs,
    embedding,
    persist_directory=DB_PATH
)

db.persist()

# Create QA system
qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(),
    retriever=db.as_retriever()
)

query = st.text_input("Ask anything from knowledge base")

if query:
    result = qa.run(query)
    st.write(result)