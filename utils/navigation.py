import importlib.util

def load_project_entry(entry_path):
    """
    Dynamically load and execute the main module for a project.
    Args:
        entry_path (str): Path to the entry point (e.g., "main.py").
    Returns:
        module: Loaded Python module.
    """
    spec = importlib.util.spec_from_file_location("project_module", entry_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
