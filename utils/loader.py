import os
import json

def load_projects(base_path="projects"):
    """Loads all project metadata from the projects directory."""
    projects = []
    for project_folder in os.listdir(base_path):
        config_path = os.path.join(base_path, project_folder, "config.json")
        if os.path.exists(config_path):
            try:
                with open(config_path, "r") as f:
                    config = json.load(f)
                    config["path"] = os.path.join(base_path, project_folder)
                    projects.append(config)
            except json.JSONDecodeError as e:
                print(f"Invalid JSON in {config_path}: {e}")
        else:
            print(f"Missing config.json in {project_folder}")
    print(f"Loaded projects: {projects}")
    return projects


