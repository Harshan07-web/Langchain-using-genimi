#retrival augmented generation

import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_chroma import Chroma

curr_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(curr_dir,"documents","deal_with_stress.txt")
persistent_dir = os.path.join(curr_dir,"db","chroma_db")

if not os.path.exists(persistent_dir):
    print("persistent dir does not exist.initializing vector store..")

    if not os.path.exists(file_path):
        raise FileNotFoundError(
        f"The file in the file path: {file_path} was not found"
        )

    loader = TextLoader(file_path,encoding="utf-8")
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000,chunk_overlap = 50,separators=["\n\n", "\n", ".", " "])
    docs = text_splitter.split_documents(documents)

    print("\n---Doc chunk info---\n")
    print(f"number of document chunks: {len(docs)}")
    print(f"Sample chunk:\n{docs[0].page_content}\n\n")

    print("\n--creating embeddings--\n")
    embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key="")
    print("\n--embedding completed--\n")

    print("\n--creating vector store--\n")
    db = Chroma.from_documents(
        docs,embedding,persist_directory=persistent_dir
    )
    print("\n--finished creating vector store--\n")

else:
    print("Vector store already exists!initialization not required")

