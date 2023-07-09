import chainlit as cl
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import DirectoryLoader
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chat_models import PromptLayerChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from dotenv import load_dotenv
load_dotenv()



@cl.langchain_factory(use_async=True)
async def init():
    msg = cl.Message(content="Processing docs...")
    await msg.send()

    loader = DirectoryLoader('data', glob="**/*.md", show_progress=True, use_multithreading=True, recursive=True)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunked_docs = splitter.split_documents(docs)
    embeddings = OpenAIEmbeddings() 


# def factory():
#     if not Path("faiss_index/index.pkl").exists():
#         raise ValueError("vectorstore does not exist, please run ingest.py first")
    
#     embeddings = OpenAIEmbeddings()
#     vectorstore = FAISS.load_local("faiss_index", embeddings)

#     llm=PromptLayerOpenAI(pl_tags=["docs-discussion"])
#     qa_chain = load_qa_chain(llm, chain_type="stuff")

#     return qa_chain

# @cl.langchain_run
# async def run(qa_chain, prompt):
#     res = qa_chain.run(prompt)
#     await cl.Message(content=res["text"]).send()
# need to send a callback when this is run to get similar documents with qa_chain.run?