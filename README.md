# 🤖 Local RAG PDF Assistant

A Retrieval-Augmented Generation (RAG) application built completely from scratch using Python, FAISS, Sentence Transformers, and a local Qwen 2.5 model.

The application allows users to ask natural language questions about one or more PDF documents. Instead of relying only on the LLM's internal knowledge, it retrieves the most relevant document chunks using semantic vector search and generates grounded answers based on the retrieved context.

This project was built by directly implementing the core RAG pipeline instead of relying on high-level frameworks such as LangChain or LlamaIndex. The goal was to gain a deeper understanding of each stage of the RAG workflow, including document processing, chunking, embedding generation, vector indexing, semantic retrieval, and grounded answer generation.

## ✨ Features

- 📄 Load and process one or more PDF documents
- ✂️ Split documents into overlapping text chunks
- 🔢 Generate semantic embeddings using Sentence Transformers
- 🗂️ Store embeddings in a FAISS vector database
- 💾 Save and load the FAISS index for faster startup
- 🔍 Perform semantic similarity search over documents
- 🤖 Generate answers using a local Qwen 2.5 model
- 💬 Interactive command-line chatbot
- 📚 Support for multiple PDF documents


## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| PyMuPDF | PDF text extraction |
| Sentence Transformers | Generate semantic embeddings |
| FAISS | Vector similarity search |
| NumPy | Numerical operations |
| Ollama | Run the local Qwen 2.5 model |
| Qwen 2.5 | Answer generation |



 ## 🏗️ Project Architecture

```text
                PDF Documents
                      │
                      ▼
              PDF Text Extraction
                      │
                      ▼
            Text Chunking + Overlap
                      │
                      ▼
      Sentence Transformer Embeddings
                      │
                      ▼
          FAISS Vector Database
                      │
         Save / Load Vector Index
                      │
                      ▼
               User Question
                      │
                      ▼
          Query Embedding Creation
                      │
                      ▼
          Semantic Similarity Search
                      │
                      ▼
          Retrieve Relevant Chunks
                      │
                      ▼
             Local Qwen 2.5 Model
                      │
                      ▼
               Generated Answer
```

## ⚙️ How It Works

1. Load one or more PDF documents.
2. Split the text into overlapping chunks.
3. Generate embeddings using Sentence Transformers.
4. Store embeddings in a FAISS vector database.
5. Convert the user's question into an embedding.
6. Retrieve the most relevant document chunks.
7. Pass the retrieved context to the local Qwen 2.5 model.
8. Generate a grounded answer.

## 📂 Project Structure

```text
Local-RAG-PDF-Assistant/
│
├── data/                 # PDF documents
├── src/                  # Source code
│   ├── chunker.py
│   ├── embeddings.py
│   ├── generator.py
│   ├── main.py
│   ├── pdf_loader.py
│   ├── retriever.py
│   ├── storage.py
│   └── vector_store.py
│
├── storage/              # Generated FAISS index (created automatically)
├── .gitignore
├── README.md
└── requirements.txt
```

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/SagarCodes03/Local-RAG-PDF-Assistant.git
cd Local-RAG-PDF-Assistant
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 4. Install the required packages

```bash
pip install -r requirements.txt
```

### 5. Install and start Ollama

Make sure Ollama is installed, then download the Qwen 2.5 model:

```bash
ollama pull qwen2.5:7b
```

### 6. Add PDF documents

Place one or more PDF files inside the `data/` folder.

Example:

```text
data/
├── attention-is-all-you-need.pdf
├── BERT.pdf
└── LLM.pdf
```

### 7. Run the application

```bash
python src/main.py
```
## 🚀 Usage

After starting the application, you can ask questions about the PDF documents placed in the `data/` folder.

Example:

```text
Ask a question: What is BERT?

Retrieved Sources:
BERT.pdf

Answer:
BERT stands for Bidirectional Encoder Representations from Transformers...
```

Type `exit` to close the application.


## 🔮 Future Improvements

- 🌐 Streamlit web interface
- 📄 Support for DOCX and TXT documents
- 📑 Page-level citations
- 💬 Conversation history
- 📊 Retrieval evaluation metrics

## 🙏 Acknowledgements

This project uses several excellent open-source tools:

- Ollama
- Qwen 2.5
- Sentence Transformers
- FAISS
- PyMuPDF

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.