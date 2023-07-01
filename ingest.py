from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import pickle
from dotenv import load_dotenv

def ingest_docs():
  loader = DirectoryLoader('data', glob="**/*.md", show_progress=True, use_multithreading=True, recursive=True)
  docs = loader.load()

  splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
  chunked_docs = splitter.split_documents(docs)

  embeddings = OpenAIEmbeddings()
  vectorstore = FAISS.from_documents(chunked_docs, embeddings)

  with open("vectorstore.pkl", "wb") as f:
     pickle.dump(vectorstore, f)

if __name__ == "__main__":
    load_dotenv()
    ingest_docs()