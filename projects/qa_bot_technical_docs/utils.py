import os
import cohere

def setup_cohere_api():
    """Initializes the Cohere API client."""
    api_key = os.getenv("COHERE_API_KEY")
    if not api_key:
        raise ValueError("COHERE_API_KEY environment variable not set!")
    return cohere.Client(api_key=api_key)

def build_answer_with_citations(response):
    """Builds an answer with citations from the Cohere chat response."""
    text = response.text
    citations = response.citations
    end = 0
    text_with_citations = ""
    for citation in citations:
        start = citation.start
        text_with_citations += text[end:start]
        end = citation.end
        citation_blocks = " [" + ", ".join([doc[4:] for doc in citation.document_ids]) + "] "
        text_with_citations += text[start:end] + citation_blocks
    text_with_citations += text[end:]
    return text_with_citations
