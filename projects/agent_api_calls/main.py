import streamlit as st
import os
import json
import re
from langchain.agents import AgentExecutor
from langchain_cohere.chat_models import ChatCohere
from langchain_cohere.react_multi_hop.agent import create_cohere_react_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.tools import tool

# Function to extract alphanumeric codes
@tool
def regex_extractor(user_query: str) -> dict:
    """Function which, given the query from the user, returns a dictionary parameter:value."""
    uuid = re.findall(r"\s([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})", user_query)
    nmgs = re.findall(r"(0000[A-Z0-9]{21})", user_query)
    objref = re.findall(r"\s([A-Z]{5,9}\d{3,4}[A-Z]{3,8})", user_query)
    urn = re.findall(r"urn:[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}", user_query)
    d = {"uuid": uuid, "nmgs": nmgs, "objref": objref, "urn": urn}
    return {k: v for k, v in d.items() if v}

regex_extractor.name = "regex_extractor"

class ExtractCodeSchema(BaseModel):
    user_query: str = Field(description="The full user query.")
regex_extractor.args_schema = ExtractCodeSchema

# Define tools and agent
tools = [regex_extractor]

preamble = """
You are an assistant that generates API requests based on user queries. Use the "regex_extractor" tool to extract codes, and construct JSON requests as instructed. Provide well-formatted JSON responses.
"""

llm = ChatCohere(model="command-r-plus", temperature=0)
prompt = ChatPromptTemplate.from_template("{input}")
agent = create_cohere_react_agent(llm=llm, tools=tools, prompt=prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

def convert_to_json(string: str) -> json:
    return json.loads(string.replace("\xa0", " ").replace("json", "").replace("`", ""))

# Streamlit App UI
def main():
    st.title("Agent API Calls")
    st.write("This project demonstrates how an agent generates API requests based on user queries.")

    user_query = st.text_area("Enter your query:", "Retrieve id 7410e652-639d-402e-984e-8fd7025f0aac...")
    if st.button("Generate API Request"):
        with st.spinner("Processing..."):
            response = agent_executor.invoke({"input": user_query, "preamble": preamble})
            formatted_response = convert_to_json(response['output'])
            st.json(formatted_response)

if __name__ == "__main__":
    main()
