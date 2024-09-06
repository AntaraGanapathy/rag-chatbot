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
