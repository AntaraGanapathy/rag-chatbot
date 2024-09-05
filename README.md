# RAG Chatbot for PDFs

## Installation
```
# Clone this repository
git clone https://github.com/mfts/papermark.git
cd papermark
```

```
# Installing the libraries (refer to requirements.txt)
pip install langchain==0.2.16
pip install pinecone==5.1.0
pip install PyPDF2==3.0.1
pip install python-dotenv==1.0.1
pip install streamlit==1.37.1
```

```
# Update API keys in .env
PINECONE_API_KEY=XXXXXXXX
HUGGINGFACE_API_KEY=XXXXXXXX
```

```
# Execution
streamlit run main.py
```
