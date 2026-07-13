import os
from pdf_loader import load_pdf
from chunker import chunk_text
from embeddings import create_embedding, model
from vector_store import create_faiss_index
from generator import generated_answer
from retriver import retrieve
from storage import save_index , load_index
print("=" * 50)
print("        Local RAG Chatbot")
print("Type 'exit' to quit")
print("=" * 50)

if os.path.exists("storage/index.faiss"):
    print("Loading existing vector database....")
    index,chunks = load_index()

else:
    print("creating vector database....")
    chunks=[]
    pdf_folder = "data"
    for file in os.listdir(pdf_folder):
        if file.endswith(".pdf"):
            pdf_path=os.path.join(pdf_folder,file)
            print(f"Loading {file}...")
            pdf_text=load_pdf(pdf_path)
            pdf_chunks = chunk_text(pdf_text)
            for i,chunk in enumerate(pdf_chunks):
                chunks.append(
                    {
                        "text":chunk,
                        "source":file,
                        "chunk_id":i
                    }
                )
    embeddings = create_embedding([chunk["text"] for chunk in chunks])
    index = create_faiss_index(embeddings)
    save_index(index, chunks)
    print("Vector database created and saved.")

while True:
    query = input("\nAsk a question: ").strip()

    if query.lower() == "exit":
        print("Goodbye!")
        break

    results = retrieve(query, model, index, chunks)

    context = "\n\n".join(result["text"] for result in results)
    print("\nRetrieved Sources:")
    for result in results:
        print(result["source"])

    answer = generated_answer(query, context)

    print("\nAnswer:\n")
    print(answer)