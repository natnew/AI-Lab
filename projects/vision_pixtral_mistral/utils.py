import requests
import streamlit as st

def analyze_image(image_url):
    """
    Send the image URL to the Pixtral API and return the analysis result.
    """
    # Get API key from Streamlit secrets
    api_key = st.secrets["pixtral"]["api_key"]
    endpoint = "https://api.pixtral.com/v1/analyze"

    # Define request headers and payload
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    data = {"image_url": image_url}

    # Send request to the Pixtral API
    response = requests.post(endpoint, headers=headers, json=data)

    # Check for errors
    if response.status_code != 200:
        error_message = response.json().get("error", "Unknown error occurred")
        raise ValueError(f"API Error: {error_message}")

    # Parse and return the analysis result
    return response.json()["insights"]
