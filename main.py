from rag import RagBot
import streamlit as st

bot = RagBot()

st.set_page_config(page_title="RAG Chatbot")
with st.sidebar:
    st.title('RAG Chatbot')


def generate_response(input):
    result = bot.rag_chain.invoke(input)
    return result.split("Answer:", 1)[1]
