import openai
import streamlit as st

def generate_text(prompt):
    # Fetch the OpenAI API key from Streamlit secrets
    api_key = st.secrets["openai"]["openai_api_key"]
    
    # Instantiate the OpenAI client
    client = OpenAI(api_key=api_key)

    # Generate the text completion
    response = client.chat.completions.create(
        model="gpt-4o",  # Replace with the correct model, e.g., `mistral-7b` if available
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ]
    )

    # Return the generated text
    return response.choices[0].message.content
