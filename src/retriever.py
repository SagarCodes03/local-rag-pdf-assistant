import numpy as np

def retrieve(query,model,index,chunks,k=3):
    query_embedding = model.encode([query])
    query_embedding = np.array(query_embedding,dtype=np.float32)
    distances,indices = index.search(query_embedding,k)
    result = []
    for idx in indices[0]:
        result.append(chunks[idx])
    return result