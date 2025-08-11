from typing import Any, Dict

class ChromaDBClient:
    def __init__(self, config_path: str):
        pass

    def connect(self) -> None:
        pass

    def create_collection(self, collection_name: str, metadata: Dict[str, Any]) -> None:
        pass

    def batch_insert_vectors(self, collection_name: str, vectors: Any, metadatas: Any) -> None:
        pass

    def search_vectors(self, collection_name: str, vector: Any, top_k: int = 5) -> Any:
        pass

    def list_collections(self) -> Any:
        pass

    def get_collection(self, collection_name: str) -> Any:
        pass

    def delete_collection(self, collection_name: str) -> None:
        pass
