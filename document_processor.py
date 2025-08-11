from typing import List, Dict

def load_support_documents(document_dir: str) -> List[Dict]:
    """
    Load and parse support documents from input directory.
    Args:
        document_dir (str): Document directory path.
    Returns:
        List[Dict]: List of loaded document contents and metadata.
    """
    pass

def preprocess_and_chunk(document: Dict) -> List[Dict]:
    """
    Clean, deduplicate, and split a support document into chunks.
    Args:
        document (Dict): Raw document dict with text and metadata.
    Returns:
        List[Dict]: List of chunk dicts (text and metadata).
    """
    pass
