import streamlit as st

from gatherer.llm.client import ask_llm

st.title("My Little Gatherer")

question = st.text_input("Ask anything")

if question:
    st.write(ask_llm(question))
    
# Initial Test: run with 
# streamlit run ui/streamlit_app.py