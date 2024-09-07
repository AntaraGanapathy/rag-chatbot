from rag import RagBot
import streamlit as st

bot = RagBot()

st.set_page_config(page_title="RAG Chatbot")
with st.sidebar:
    st.title('RAG Chatbot')


def generate_response(input):
    result = bot.rag_chain.invoke(input)
    return result.split("Answer:", 1)[1]


if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "Welcome, let's unveil your future"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if input := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": input})
    with st.chat_message("user"):
        st.write(input)
