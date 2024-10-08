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
    st.session_state.messages = [{"role": "assistant", "content": "Welcome! Let's unveil the future of AI together... "}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if input := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": input})
    with st.chat_message("user"):
        st.write(input)

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Generating answer.."):
            response = generate_response(input)
            st.write(response)
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)
