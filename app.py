import streamlit as st 
from openai import OpenAI
import chatLLM

st.title('A RAG based ChatBot')
st.caption("Yes, I answer questions based on your data, and ofcourse in general")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role" : "chatbot", "content": "Hi User"}]

for texts in st.session_state.messages:
    st.chat_message(texts['role']).write(texts['content'])
    
if query := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": query})
    st.chat_message("user").write(query)
    response = chatLLM.chat(query)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)


    