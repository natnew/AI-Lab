import streamlit as st
from projects.code_generation_codestral.utils import generate_code

def run():
    st.title("Code Generation with Codestral")
    st.write("""
    Codestral is a cutting-edge generative model specifically designed for code generation tasks, 
    including fill-in-the-middle and code completion. With training on 80+ programming languages, 
    Codestral can handle both common and less common languages with ease.
    """)

    # Input for the code task or snippet
    code_task = st.text_area("Enter your code snippet or description", placeholder="Type your code-related task here...")

    if st.button("Generate Code"):
        if code_task.strip():
            with st.spinner("Generating code..."):
                try:
                    generated_code = generate_code(code_task)
                    st.subheader("Generated Code")
                    st.code(generated_code, language="python")  # Default to Python; adjust as needed
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a valid input.")
