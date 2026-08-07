import streamlit as st


def render_question_form() -> tuple[str, bool]:
    with st.form("ask_form"):
        question = st.text_area(
            "Question",
            placeholder="Ask the local model something...",
            height=120,
        )
        submitted = st.form_submit_button("Ask", type="primary")

    return question, submitted
