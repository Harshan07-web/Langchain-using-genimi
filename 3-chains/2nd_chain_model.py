from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda,RunnableSequence

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

prompt_template = ChatPromptTemplate.from_messages([
    ("system","you are a fact expert who tells facts about {topic}."),
    ("human","Tell me {fact_count} facts.")
])

format_prompt = RunnableLambda(lambda x: prompt_template.format_prompt(**x))
invoke_model =  RunnableLambda(lambda x: model.invoke(x.to_messages()))
parse_output = RunnableLambda(lambda x: x.content)

chain = RunnableSequence(first=format_prompt,middle=[invoke_model],last=parse_output)

response =  chain.invoke({"topic":"airways","fact_count":3})

print(response)