import os
import torch
import streamlit as st
from datasets import load_dataset
import cohere

# Function to initialize Cohere client using the environment variable
def setup_cohere_client():
    api_key = os.getenv("CO_API_KEY")
    if not api_key:
        raise ValueError("Cohere API key is not set. Please set the CO_API_KEY environment variable in Streamlit Cloud settings.")
    return cohere.Client(api_key)

# Main function for the Streamlit app
def main():
    # Tags Information Box
    st.info("**Tags:** semantic search, Wikipedia, Cohere embeddings")

    # Expandable "How it works" Section
    with st.expander("How it works"):
        st.markdown("""
        1. **Load Wikipedia Embeddings**: The app loads 1,000 pre-embedded Wikipedia documents and stores their embeddings.
        2. **Input Query**: Enter a question or query in the input box provided.
        3. **Generate Query Embedding**: The app uses Cohere's embedding model to convert the query into a vector representation.
        4. **Perform Search**: The app computes the similarity between the query and document embeddings using dot product.
        5. **Display Results**: The top 3 relevant documents are displayed based on the similarity score.
        """)


    # Initialize Cohere client
    co = setup_cohere_client()

    # Load dataset and embeddings
    st.info("Loading Wikipedia embeddings...")
    max_docs = 1000
    docs_stream = load_dataset("Cohere/wikipedia-22-12-simple-embeddings", split="train", streaming=True)
    
    docs = []
    doc_embeddings = []
    for doc in docs_stream:
        docs.append(doc)
        doc_embeddings.append(doc['emb'])
        if len(docs) >= max_docs:
            break
    doc_embeddings = torch.tensor(doc_embeddings)
    
    st.success("Loaded Wikipedia embeddings.")
    
    # User input for search query
    query = st.text_input("Enter your search query:", "Who founded Wikipedia?")
    
    if st.button("Search"):
        with st.spinner("Searching..."):
            # Generate embedding for the query
            response = co.embed(texts=[query], model="multilingual-22-12")
            query_embedding = torch.tensor(response.embeddings)
            
            # Perform semantic search using dot product
            dot_scores = torch.mm(query_embedding, doc_embeddings.transpose(0, 1))
            top_k = torch.topk(dot_scores, k=3)
            
            st.subheader("Search Results")
            for doc_id in top_k.indices[0].tolist():
                st.write(f"**Title:** {docs[doc_id]['title']}")
                st.write(f"{docs[doc_id]['text']}\n")
    
if __name__ == "__main__":
    main()
