from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda,RunnableSequence,RunnableParallel
from langchain.schema.output_parser import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

summary_template = ChatPromptTemplate.from_messages([
    ("system","You are a movie critic"),
    ("human","Provide the summary of the movie {movie_name}.")
])

def analyze_plot(text : str):
    plot_template = ChatPromptTemplate.from_messages([
        ("system","you are a movie critic"),
        ("human","analyze the plot: {plot},provide the strength and weakness of the movie")
    ])
    return plot_template.format_prompt(plot = text)

def character_analyze(character):
    character_template = ChatPromptTemplate.from_messages([
        ("system","you are a movie critic"),
        ("human","analyze the character: {characters}.What are their strengths and weakness")
    ])
    return character_template.format_prompt(characters = character)

def combine_chains(plot_analysis,character_analysis):
    return f"plot analysis:\n{plot_analysis}\n\nCharacter analysis:\n{character_analysis}"

plot_chain = (
    RunnableLambda(lambda x: analyze_plot(x)) | model | StrOutputParser()
    )

character_chain = (
    RunnableLambda(lambda x: character_analyze(x)) | model | StrOutputParser()
    )

combine_chain = (
    summary_template | model | StrOutputParser() 
    | RunnableParallel(branches={"plot":plot_chain,"characters":character_chain})
    | RunnableLambda(lambda x: combine_chains(x["branches"]["plot"],x["branches"]["characters"]))
)

result = combine_chain.invoke({"movie_name":"Rush Hour 1"})

print(result)