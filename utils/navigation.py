import importlib.util
import cohere

def setup_cohere_api(api_key: str = None):
    """
    Initializes the Cohere client.
    :param api_key: Your Cohere API key. If not provided, it uses the CO_API_KEY environment variable.
    """
    if not api_key:
        import os
        api_key = os.getenv("CO_API_KEY")
    if not api_key:
        raise ValueError("Cohere API key is not set. Please set the CO_API_KEY environment variable or pass it explicitly.")
    return cohere.Client(api_key=api_key)

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
