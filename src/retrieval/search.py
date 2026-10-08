def search(query, model, index, chunks, k=5):
    query = model.encode_query(query)
    query = query.reshape(1, -1)
    distances, indices = index.search(query, k)
    indices = indices.flatten()
    
    results = []
    for idx in indices:
        results.append(chunks[idx])
    print(results)
    return results