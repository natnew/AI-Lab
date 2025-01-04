import streamlit as st
from projects.text_generation_mistral.utils import generate_text

def run():
    st.title("Text Generation with Mistral")
    st.write("""
    The Mistral model allows you to generate responses based on a given prompt. 
    Enter your prompt below and see the AI's response.
    """)

    # Input section
    prompt = st.text_area("Enter your prompt", placeholder="Type your message here...")

    if st.button("Generate Response"):
        if prompt.strip():
            with st.spinner("Generating response..."):
                try:
                    response = generate_text(prompt)
                    st.subheader("Generated Response")
                    st.write(response)
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a valid prompt.")
