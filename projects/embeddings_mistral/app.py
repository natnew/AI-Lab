import streamlit as st
from projects.embeddings_mistral.utils import generate_embeddings, calculate_similarity

def run():
    st.title("Embeddings with Mistral AI")
    st.write("""
    Embeddings are vectorial representations of text that capture semantic meaning. Mistral AI's 
    embeddings API offers state-of-the-art embeddings for text, which can be used for NLP tasks 
    like clustering and classification.
    """)

    # Input section
    text1 = st.text_area("Enter the first text", placeholder="Type the first text here...")
    text2 = st.text_area("Enter the second text (optional)", placeholder="Type the second text here...")

    if st.button("Generate Embeddings"):
        if text1.strip():
            with st.spinner("Generating embeddings..."):
                try:
                    # Generate embeddings for the first text
                    embeddings1 = generate_embeddings([text1])
                    st.subheader("First Text Embeddings")
                    st.write(embeddings1)

                    # If a second text is provided, calculate similarity
                    if text2.strip():
                        embeddings2 = generate_embeddings([text2])
                        similarity = calculate_similarity(embeddings1, embeddings2)
                        st.subheader("Second Text Embeddings")
                        st.write(embeddings2)

                        st.subheader("Similarity Score")
                        st.write(f"Cosine Similarity: {similarity:.4f}")
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter valid text for the first field.")
