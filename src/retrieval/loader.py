from pathlib import Path


def load_document(file_path: str) -> str:
    """Load a text document and return its contents."""


    #file_path = "data/knowledge_base/support_faq.txt"

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    return path.read_text(encoding="utf-8")