import streamlit as st

from gatherer.llm.client import LLMError, ask_llm

st.title("My Little Gatherer")

with st.sidebar:
    st.header("Generation")
    temperature = st.slider("Temperature", 0.0, 2.0, 0.7, 0.1)
    top_p = st.slider("Top-p", 0.01, 1.0, 0.95, 0.01)
    max_tokens = st.number_input("Maximum output tokens", 1, 4096, 512, 1)

with st.form("ask_form"):
    question = st.text_area(
        "Question",
        placeholder="Ask the local model something...",
        height=120,
    )
    submitted = st.form_submit_button("Ask", type="primary")

if submitted:
    try:
        with st.spinner("Thinking..."):
            answer = ask_llm(
                question,
                temperature=temperature,
                top_p=top_p,
                max_tokens=int(max_tokens),
            )
        st.write(answer)
    except ValueError as error:
        st.warning(str(error))
    except LLMError as error:
        st.error(str(error))

# Initial Test: run with 
# streamlit run ui/streamlit_app.py