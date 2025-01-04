import openai
import streamlit as st

def generate_text(prompt):
    openai.api_key = st.secrets["openai_api_key"]

    if not openai.api_key:
        raise ValueError("API key is missing. Please configure it in Streamlit secrets.")

    response = openai.ChatCompletion.create(
        model="mistral-7b-chat",
        messages=[{"role": "user", "content": prompt}],
    )
    return response['choices'][0]['message']['content']
