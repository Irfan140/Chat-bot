import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()


## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful massistant . Please  repsonse to the user queries"),
        ("user","Question:{question}")
    ]
)

# Function to generate response using OpenAI API
# temperature is a parameter that controls the randomness of the output

# suppose temperature is 0.0, the model will always return the same output for a given input
# if temperature is 1.0, the model will return more random output
def generate_response(question,api_key,engine,temperature,max_tokens):

    llm = ChatOpenAI(model=engine, openai_api_key=api_key)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({'question':question})
    return answer


## Title of the app
st.title("Q&A Chatbot With OpenAI")



## Sidebar for settings
st.sidebar.title("Settings")
api_key=st.sidebar.text_input("Enter your Open AI API Key:",type="password")


## Select the OpenAI model
engine=st.sidebar.selectbox("Select Open AI model",["gpt-4o","gpt-4-turbo","gpt-4"])


## Adjust response parameter
# value=0.7 will be the default value
temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)



## Main interface for user input
st.write("Go ahead and ask any question")
user_input=st.text_input("You:")


if user_input and api_key:
    response=generate_response(user_input,api_key,engine,temperature,max_tokens)
    st.write(response)

elif user_input:
    st.warning("Please enter the OPen AI API Key in the sider bar")
else:
    st.write("Please provide the user input")


