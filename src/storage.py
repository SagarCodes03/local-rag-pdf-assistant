import faiss
import pickle

def save_index(index,chunks):
    faiss.write_index(index,"storage/index.faiss")

    with open("storage/chunks.pkl","wb") as file:
        pickle.dump(chunks,file)
    
def load_index():
    index=faiss.read_index("storage/index.faiss")

    with open("storage/chunks.pkl","rb") as file:
        chunks= pickle.load(file)
    
    return index , chunks
