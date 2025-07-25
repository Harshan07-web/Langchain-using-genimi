from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain import hub
from langchain.agents import create_react_agent , AgentExecutor , tool
import datetime

load_dotenv()

@tool
def get_sys_time(format: str = "%Y-%m-%d %H-%M-%S"):
    """returns the current date and time in a specified format"""

    curr_time = datetime.datetime.now()
    formatted_time = curr_time.strftime(format)
    return formatted_time


model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

query = "what will be the time after 5hours from now?"

template = hub.pull("hwchase17/react")
tools =[get_sys_time]

agent = create_react_agent(model,tools , template)
agent_executer = AgentExecutor(agent=agent,tools=tools,verbose=True)

result = agent_executer.invoke({"input":query})
