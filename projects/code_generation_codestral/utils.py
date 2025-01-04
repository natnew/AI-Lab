import requests
import streamlit as st

def generate_code(code_task):
    """
    Send the code task or snippet to the Codestral API and return the generated code.
    """
    api_key = st.secrets["codestral"]["api_key"]
    endpoint = "https://api.codestral.com/v1/generate"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    data = {"task": code_task}

    response = requests.post(endpoint, headers=headers, json=data)

    if response.status_code != 200:
        raise ValueError(f"API Error: {response.json().get('error', 'Unknown error')}")

    return response.json()["generated_code"]
