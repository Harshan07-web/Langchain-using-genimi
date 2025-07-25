#simple message passing to the bot

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage,SystemMessage

load_dotenv()

messages = [
        SystemMessage(content="Solve the following math problems"),
        HumanMessage(content="what is the square root of 49?"),
]

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
result = model.invoke(messages)
print(f"Answer from google: {result.content}")