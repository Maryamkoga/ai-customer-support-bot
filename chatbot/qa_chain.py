import os
from dotenv import load_dotenv
from transformers import pipeline
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

def load_docs():
    loader = DirectoryLoader("./data", glob="*.md", use_multithreading=True)
    documents = loader.load()
    return documents

def setup_chain():
    documents = load_docs()
    # Smaller chunks for better relevance
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = FAISS.from_documents(docs, embeddings)
    return db

# Initialize generator globally
generator = pipeline("text2text-generation", model="google/flan-t5-base")

def ask_bot(db, question):
    # Retrieve the most relevant document
    docs = db.similarity_search(question, k=1)

    # If no relevant docs were found, return a fallback
    if not docs:
        return "Sorry, I don't know."

    # Combine the content into context
    context = "\n".join([doc.page_content for doc in docs])

    # Instructional prompt to reduce hallucination
    prompt = (
        f"Context:\n{context}\n\n"
        f"Question: {question}\n"
        "Only answer if the context clearly contains the answer. "
        "If not, say: 'Sorry, I don't know.' Do not guess or include unrelated information.\n"
        "Answer:"
    )

    # Generate response
    output = generator(prompt, max_new_tokens=100)

    # Extract generated text
    answer = output[0]['generated_text']
    return answer



    






