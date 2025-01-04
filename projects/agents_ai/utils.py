import openai
import streamlit as st

def create_role_playing_conversation(agent_1, agent_2, scenario):
    """
    Create a role-playing conversation between two agents using the AI API.
    """
    api_key = st.secrets["openai"]["api_key"]

    # Initialize OpenAI client
    openai.api_key = api_key

    # Construct the prompt for role-playing conversation
    messages = [
        {"role": "system", "content": f"You are {agent_1}, a stand-up comedian."},
        {"role": "system", "content": f"You are {agent_2}, another stand-up comedian."},
        {"role": "user", "content": f"Scenario: {scenario}"},
    ]

    # Call OpenAI API for conversation
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0.9,
    )

    # Extract the conversation
    return response.choices[0].message.content
