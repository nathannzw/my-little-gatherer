import streamlit as st

from gatherer.llm.client import LLMError, ask_llm
from gatherer.ui.chat import render_question_form
from gatherer.ui.generation import render_generation_settings

st.title("My Little Gatherer")

generation_settings = render_generation_settings()
question, submitted = render_question_form()

if submitted:
    try:
        with st.spinner("Thinking..."):
            answer = ask_llm(
                question,
                temperature=generation_settings.temperature,
                top_p=generation_settings.top_p,
                max_tokens=generation_settings.max_tokens,
            )
        st.write(answer)
    except ValueError as error:
        st.warning(str(error))
    except LLMError as error:
        st.error(str(error))

# Initial Test: run with 
# streamlit run ui/streamlit_app.py