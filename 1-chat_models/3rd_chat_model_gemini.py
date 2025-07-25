#having a conversation with the bot

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.schema import AIMessage , HumanMessage, SystemMessage

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

chat_history=[]

system_message = SystemMessage(content="you are a helpful AI assistant.")
chat_history.append(system_message)

while True:
    query = input("You: ")
    if query.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=query))

    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))

    print(f"Ai: {response}")

print("\n\n---------history---------")
print(chat_history)