import streamlit as st
from projects.text_generation_mistral.app import run as mistral_run

# Map of project titles to their corresponding run functions
PROJECTS = {
    "Text Generation with Mistral": mistral_run,
    # Add more projects here as needed
}

def main():
    st.sidebar.title("Project Selector")
    selected_project = st.sidebar.selectbox("Choose a project", list(PROJECTS.keys()))

    # Run the selected project
    PROJECTS[selected_project]()

if __name__ == "__main__":
    main()
