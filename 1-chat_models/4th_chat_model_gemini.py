#improved model of the bot which stores history in a firebase database 

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.schema import AIMessage , HumanMessage, SystemMessage
from langchain_google_firestore import FirestoreChatMessageHistory
from google.cloud import firestore

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

PROJECT_ID = "langchain-8d875"
SESSION_ID ="new_session"
COLLECTION_NAME = "chat_history"

print("initializing firebase")
client = firestore.Client(project=PROJECT_ID)

print("initializing firestore chat message history..")

chat_history = FirestoreChatMessageHistory(
    session_id = SESSION_ID,
    collection = COLLECTION_NAME,
    client = client)

print("chat histiry initialized")
print("Current chat history: ",chat_history.messages)

print("Start chatting with the ai,type 'exit' to quit the chat")

while True:
    query = input("You: ")
    if query.lower() == "exit":
        break
    chat_history.add_user_message(query)

    result = model.invoke(chat_history.messages)
    response = result.content
    chat_history.add_ai_message(response)

    print(f"Ai: {response}")

