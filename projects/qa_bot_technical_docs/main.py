import streamlit as st
from projects.qa_bot_technical_docs.retriever import initialize_retriever, retrieve_documents
from utils import setup_cohere_api, build_answer_with_citations

from utils import setup_cohere_api, build_answer_with_citations
import cohere
import json

def main():
    # Setup Streamlit UI
    # Tags Information Box
    st.info("**Tags:** qa, cohere, technical documentation")

    # Expandable "How it works" Section
    with st.expander("How it works"):
        st.write("""
        The **QA Bot for Technical Documentation** project helps answer user questions based on technical documentation using Cohere embeddings and LlamaIndex. Here’s how it works:
        
        1. **Data Embedding**:
        - Technical documentation is embedded into a vector database using Cohere’s `embed-english-v3.0` model.
        2. **Document Retrieval**:
        - A retriever searches the vector database for the most relevant documents based on the user’s question.
        3. **Cohere Chat**:
        - The retrieved documents are passed to Cohere’s `command-r` model to generate a grounded answer.
        4. **Answer with Citations**:
        - The answer is displayed along with citations referencing the most relevant documents.
        """)


    # Initialize Cohere API and retriever
    co = setup_cohere_api()
    retriever = initialize_retriever(co)

    # User query input
    user_query = st.text_input("Enter your question:", "")
    if st.button("Get Answer"):
        with st.spinner("Processing..."):
            try:
                # Retrieve relevant documents
                documents = retrieve_documents(retriever, user_query)
                st.write("Top documents retrieved:", documents[:3])  # Display top 3 documents

                # Use Cohere's chat endpoint to generate an answer
                response = co.chat(
                    message=user_query,
                    model="command-r",
                    temperature=0.0,
                    documents=documents
                )
                grounded_answer = build_answer_with_citations(response)
                st.write("Answer with citations:")
                st.markdown(grounded_answer)
            except Exception as e:
                st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
