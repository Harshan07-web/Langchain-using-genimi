#basic question and response from bot

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

message = "What is 2+2?"

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
result = model.invoke(message)

print(result)