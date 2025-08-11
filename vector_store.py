from typing import List, Dict, Any

def upsert_support_chunks(collection_name: str, chunk_texts: List[str], embeddings: List[Any], metadatas: List[Dict]) -> None:
    """
    Insert or update chunks and their vectors plus metadata in the vector db.
    Args:
        collection_name (str): Collection or namespace.
        chunk_texts (List[str]): List of document chunk texts.
        embeddings (List[Any]): Chunk embeddings.
        metadatas (List[Dict]): Metadata for each chunk.
    Returns:
        None
    """
    pass

def search_support_chunks(collection_name: str, query_embedding: Any, top_k: int = 5) -> List[Dict]:
    """
    Vector similarity search for support chunks.
    Args:
        collection_name (str): Target collection.
        query_embedding (Any): Embedding for the user query.
        top_k (int): Number of results.
    Returns:
        List[Dict]: Retrieved chunks and metadata.
    """
    pass
