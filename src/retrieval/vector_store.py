import faiss


def create_vector_store(embeddings):
    index = faiss.IndexFlatL2(len(embeddings[0]))
    index.add(embeddings)
    return index