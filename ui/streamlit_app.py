import streamlit as st

from gatherer.llm.client import LLMError, ask_llm
from components.chat import render_question_form
from components.generation import render_generation_settings
from components.request_log import render_request_log

st.title("My Little Gatherer")

generation_settings = render_generation_settings()
question, submitted = render_question_form()
render_request_log(st.session_state.get("last_request"))

if submitted:
    try:
        with st.spinner("Thinking..."):
            result = ask_llm(
                question,
                temperature=generation_settings.temperature,
                top_p=generation_settings.top_p,
                max_tokens=generation_settings.max_tokens,
            )
        st.session_state.last_request = result
        st.write(result.answer)
        render_request_log(result)
    except ValueError as error:
        st.warning(str(error))
    except LLMError as error:
        st.error(str(error))

# Run with:
# streamlit run ui/streamlit_app.py
