from src.retrieval.loader import load_document
from src.retrieval.chunker import split_text
from src.retrieval.embedding import create_embeddings
from src.retrieval.vector_store import create_vector_store
from src.retrieval.search import search

file_path = "data/knowledge_base/support_faq.txt"

chunks = split_text(load_document(file_path))

embeddings = create_embeddings(chunks)

print(create_vector_store(embeddings))

