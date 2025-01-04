import streamlit as st
from projects.text_generation_mistral.app import run as mistral_run
from projects.vision_pixtral_mistral.app import run as pixtral_run
from projects.code_generation_codestral.app import run as codestral_run
from projects.embeddings_mistral.app import run as embeddings_run
from projects.agents_ai.app import run as agents_run

# Map of project titles to their corresponding run functions
PROJECTS = {
    "Text Generation with Mistral": mistral_run,
    "Vision with Pixtral with Mistral": pixtral_run,
    "Code Generation with Codestral": codestral_run,
    "Embeddings with Mistral AI": embeddings_run,
    "AI Agents": agents_run,
    # Add more projects here as needed
}

def main():
    st.sidebar.title("Project Selector")
    selected_project = st.sidebar.selectbox("Choose a project", list(PROJECTS.keys()))

    # Run the selected project
    PROJECTS[selected_project]()

if __name__ == "__main__":
    main()
