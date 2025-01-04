import streamlit as st
from utils.loader import load_projects
from utils.navigation import load_project_entry
import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Load all projects
projects = load_projects()

# Handle empty projects
if not projects:
    st.sidebar.warning("No projects found. Please add valid projects to the 'projects' folder.")

# Sidebar Navigation
st.sidebar.title("AI-Lab Projects")
project_names = [project["name"] for project in projects]
selected_project = st.sidebar.selectbox("Select a Project", project_names)

# Display Selected Project Details
for project in projects:
    if project["name"] == selected_project:
        st.title(project["name"])
        st.write(project["description"])
        

        # Load and Run the Project
        entry_point = project["path"] + "/" + project["entry_point"]
        if st.button(f"Run {project['name']}"):
            st.write("Running project...")
            module = load_project_entry(entry_point)
            # Assuming the project entry point has a `main()` function
            module.main()
