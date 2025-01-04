import requests
import numpy as np
import streamlit as st

def generate_embeddings(texts):
    """
    Send a list of texts to the Mistral Embeddings API and return the embeddings.
    """
    api_key = st.secrets["mistral"]["api_key"]
    endpoint = "https://api.mistral.com/v1/embeddings"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    data = {"texts": texts, "model": "mistral-embed"}

    response = requests.post(endpoint, headers=headers, json=data)

    if response.status_code != 200:
        raise ValueError(f"API Error: {response.json().get('error', 'Unknown error')}")

    return response.json()["embeddings"]

def calculate_similarity(embedding1, embedding2):
    """
    Calculate the cosine similarity between two embeddings.
    """
    embedding1 = np.array(embedding1[0])
    embedding2 = np.array(embedding2[0])

    dot_product = np.dot(embedding1, embedding2)
    norm1 = np.linalg.norm(embedding1)
    norm2 = np.linalg.norm(embedding2)

    return dot_product / (norm1 * norm2)
