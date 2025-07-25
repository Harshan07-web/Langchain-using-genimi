from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

prompt_template = ChatPromptTemplate.from_messages([
    ("system","you are a fact expert who tells facts about {topic}."),
    ("human","Tell me {fact_count} facts.")
])

chain = prompt_template | model | StrOutputParser()

result = chain.invoke({"topic":"airways","fact_count":3})

print(result)
