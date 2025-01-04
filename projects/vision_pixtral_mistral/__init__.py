import requests
import streamlit as st

def analyze_image(image_url):
    """
    Send the image URL to the Pixtral 12B API and return the analysis result.
    """
    api_key = st.secrets["pixtral"]["api_key"]
    endpoint = "https://api.pixtral.com/v1/analyze"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    data = {"image_url": image_url}

    response = requests.post(endpoint, headers=headers, json=data)

    if response.status_code != 200:
        raise ValueError(f"API Error: {response.json().get('error', 'Unknown error')}")

    return response.json()["insights"]
