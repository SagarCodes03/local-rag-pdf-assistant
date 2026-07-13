import faiss
import numpy as np 


def create_faiss_index(embeddings):
    embeddings = np.array(embeddings , dtype=np.float32)
    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    return index