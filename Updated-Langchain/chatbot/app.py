from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY") #os environment Take the API key stored in my system and make it available to this Python program.
## Langsmith tracking: os interact with the operating system to set environment variables that enable Langsmith tracing and provide the API key for authentication. This allows the program to track and log interactions with the OpenAI API for debugging and analysis purposes.
os.environ["LANGCHAIN_TRACING_V2"]="true"#Enable Langsmith tracing version 2, which allows for more detailed tracking of interactions with the OpenAI API.
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY") 

## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework makes the UI without any html code and it is very easy to use and learn. It is a open source framework for building web applications in python. It is very popular among data scientists and machine learning engineers because it allows them to quickly build and deploy web applications without any front-end development skills.

st.title('Langchain Demo With OPENAI API') 
input_text=st.text_input("Search the topic u want")

# openAI LLm 
llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text})) #wrote the langchain..