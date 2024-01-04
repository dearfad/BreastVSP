from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

directory_loader = DirectoryLoader('static/documents')
documents = directory_loader.load()
character_text_splitter = CharacterTextSplitter(chunk_size=368, chunk_overlap=8)
splitted_documents = character_text_splitter.split_documents(documents)
embeddings = HuggingFaceEmbeddings(model_name='shibing624/text2vec-base-chinese',model_kwargs={'device':'cuda:0'},encode_kwargs={'normalize_embeddings':False})

db = Chroma.from_documents(splitted_documents, persist_directory='VectorStore', embedding=embeddings)
db.persist()