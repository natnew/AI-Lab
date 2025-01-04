import datasets
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.embeddings.cohere import CohereEmbedding
from pathlib import Path
from llama_index.core.schema import TextNode

def initialize_retriever(co):
    """Initializes the retriever with Cohere embeddings and rerank."""
    path_index = Path(".") / "aws-documentation_index_cohere"
    embed_model = CohereEmbedding(
        cohere_api_key=co.api_key,
        model_name="embed-english-v3.0"
    )
    
    if path_index.exists():
        storage_context = StorageContext.from_defaults(persist_dir=path_index)
        index = load_index_from_storage(storage_context, embed_model=embed_model)
    else:
        # Load dataset and build index (takes time!)
        data = datasets.load_dataset("sauravjoshi23/aws-documentation-chunked")
        stub_len = len("https://github.com/siagholami/aws-documentation/tree/main/documents/")
        documents = [
            TextNode(
                text=sample["text"],
                title=sample["source"][stub_len:],
                id_=sample["id"]
            ) for sample in data["train"]
        ]
        index = VectorStoreIndex(documents, embed_model=embed_model)
        index.storage_context.persist(path_index)
    
    retriever = index.as_retriever(similarity_top_k=60)
    return retriever

def retrieve_documents(retriever, query, top_n=20):
    """Retrieves top documents for a query."""
    nodes = retriever.retrieve(query)
    documents = [{"text": node.node.text, "llamaindex_id": node.node.id_} for node in nodes]
    return documents
