from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda,RunnableSequence
from langchain.schema.output_parser import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

fact_template = ChatPromptTemplate.from_messages([
    ("system","you are a fact expert who tells facts about {topic}."),
    ("human","Tell me {fact_count} facts.")
])

translation_template = ChatPromptTemplate([
    ("system","You are a translator and convert the provided text into {language}"),
    ("human","Translate the following text to {language}:{text}")
])

fact_chain = fact_template | model | StrOutputParser()

def trans_fun(text:str):
    return translation_template.invoke({"language":"spanish","text":text})

trans_chain =  RunnableLambda(trans_fun) | model | StrOutputParser()

full_chain = fact_chain | trans_chain

result = full_chain.invoke({"topic":"railways","fact_count":3})
print(result)