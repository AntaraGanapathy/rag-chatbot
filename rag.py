from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import HuggingFaceHub
from dotenv import load_dotenv
from data import pdf_to_text
import os
from langchain.vectorstores import Pinecone
from pinecone import Pinecone as pinecone
from pinecone import ServerlessSpec
from langchain import PromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser


class ChatBot():
    input_path = './sample.pdf'

    output_path = './sample.txt'

    pdf_to_text(input_path, output_path)

    load_dotenv()

    loader = TextLoader('./sample.txt')
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=4)
    docs = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings()

    pc = pinecone(api_key=os.getenv('PINECONE_API_KEY'))

    index_name = "pdf-rag"

    if index_name not in pc.list_indexes().names():
        pc.create_index(name=index_name, metric="cosine", dimension=768, spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        ))
        docsearch = Pinecone.from_documents(docs, embeddings, index_name=index_name)
    else:
        docsearch = Pinecone.from_existing_index(index_name, embeddings)