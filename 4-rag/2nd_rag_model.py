import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

curr_dir = os.path.dirname(os.path.abspath(__file__))
persistent_dir = os.path.join(curr_dir,"db","chroma_db")

embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key="")

db = Chroma(persist_directory=persistent_dir,embedding_function=embedding)

query = "what causes stress among most of the people?"

retriver = db.as_retriever(
    search_type = "similarity_score_threshold",
    search_kwargs = {"k":3,"score_threshold":0.5}
)

relevant_docs = retriver.invoke(query)

print("\n---relevant docs---\n")
for i,doc in enumerate(relevant_docs,1):
    print(f"document{i}:\n{doc.page_content}\n")
    if doc.metadata:
        print(f"Source: {doc.metadata.get('source',"unknown")}\n")
