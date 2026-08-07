from gatherer.llm.client import LLMResult

import streamlit as st


def render_request_log(result: LLMResult | None) -> None:
    with st.sidebar:
        st.divider()
        st.subheader("Last request")

        if result is None:
            st.caption("No completed request yet.")
            return

        st.caption(f"Model: `{result.model}`")
        st.metric("Response time", f"{result.elapsed_seconds:.1f} s")
        st.metric("Output", f"{result.output_chars:,} characters")
        st.caption(f"Finish reason: `{result.finish_reason or 'unknown'}`")
        st.caption(f"Prompt: {result.prompt_chars:,} characters")

        if result.total_tokens is not None:
            st.caption(
                "Tokens: "
                f"{result.prompt_tokens or 0:,} prompt + "
                f"{result.completion_tokens or 0:,} output = "
                f"{result.total_tokens:,} total"
            )
        else:
            st.caption("Token usage was not provided by the model server.")