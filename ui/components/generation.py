from dataclasses import dataclass

import streamlit as st


@dataclass(frozen=True)
class GenerationSettings:
    temperature: float
    top_p: float
    max_tokens: int


def render_generation_settings() -> GenerationSettings:
    with st.sidebar:
        st.header("Generation settings")
        temperature = st.slider(
            "Temperature",
            min_value=0.0,
            max_value=2.0,
            value=0.7,
            step=0.1,
        )
        top_p = st.slider(
            "Top-p",
            min_value=0.01,
            max_value=1.0,
            value=0.95,
            step=0.01,
        )
        max_tokens = st.number_input(
            "Maximum output tokens",
            min_value=1,
            max_value=4096,
            value=2048,
            step=1,
        )

        with st.expander("What should I use?"):
            st.markdown(
                """
                These are **generation settings**, also commonly called
                **sampling hyperparameters**. They control how the model chooses
                tokens for each response.

                **Good starting point**

                - Temperature: `0.7`
                - Top-p: `0.95`
                - Maximum output tokens: `2048`

                **Temperature**

                Lower values make responses more predictable and focused. Use
                `0.0-0.3` for extraction, classification, or code. Use
                `0.7-1.0` for normal conversation. Higher values create more
                variation but can also make answers less reliable.

                **Top-p**

                This limits token choices to a probability pool. `0.95` is a
                sensible default. Lower values make output more focused. Usually
                change either temperature or top-p while experimenting, rather
                than changing both at once.

                **Maximum output tokens**

                This is a response length limit, not a creativity setting. Use
                `256-512` for short answers, `1024-2048` for explanations, and
                higher values for long code or documents. Larger values can take
                longer and consume more memory.

                The server's `min-p` remains controlled by `start_model.bat`.
                `gpu-layers` is a hardware/performance setting, not a response
                quality setting.
                """
            )

    return GenerationSettings(
        temperature=temperature,
        top_p=top_p,
        max_tokens=int(max_tokens),
    )
