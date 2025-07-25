from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

"""template = "write a {tone} email to {company} expressing interest in the {position} position,mentioning {skill} as a key strength" \
"keep it to 4 lines max"

prompt_template = ChatPromptTemplate.from_template(template)

prompt = prompt_template.invoke({
    "tone":"formal",
    "company":"Samsung",
    "position":"AI engineer",
    "skill":"AI"
})

result = model.invoke(prompt)
response = result.content

print(response)"""

messages = [
    ("system","you are a comedian who tells jokes about {topic}."),
    ("human","Tell me {joke_count} jokes.")
]

prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic":"developers","joke_count":3})

result = model.invoke(prompt)
response = result.content
print(response)