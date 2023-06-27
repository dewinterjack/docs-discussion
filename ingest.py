from langchain.document_loaders import DirectoryLoader

loader = DirectoryLoader('data/docs', glob="**/*.md", show_progress=True, use_multithreading=True, recursive=True)
docs = loader.load()

print(docs[0])