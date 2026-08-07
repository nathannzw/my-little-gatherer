from openai import OpenAI
from openai import APIConnectionError, APIStatusError, APITimeoutError

from gatherer.core.config import settings


class LLMError(RuntimeError):
    """An expected failure while communicating with the model server."""


client = OpenAI(
    base_url=settings.llm_url,
    api_key="not-required",
    timeout=60.0,
)


def ask_llm(
    prompt: str,
    *,
    temperature: float = 0.7,
    top_p: float = 0.95,
    max_tokens: int = 512,
) -> str:
    prompt = prompt.strip()
    if not prompt:
        raise ValueError("Please enter a question before sending it.")
    if len(prompt) > 10_000:
        raise ValueError("Please keep your question under 10,000 characters.")
    if not 0.0 <= temperature <= 2.0:
        raise ValueError("Temperature must be between 0 and 2.")
    if not 0.0 < top_p <= 1.0:
        raise ValueError("Top-p must be greater than 0 and no more than 1.")
    if not 1 <= max_tokens <= 4_096:
        raise ValueError("Maximum output tokens must be between 1 and 4,096.")

    try:
        response = client.chat.completions.create(
            model=settings.model_name,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            top_p=top_p,
            max_tokens=max_tokens,
        )
    except APITimeoutError as error:
        raise LLMError("The model took too long to respond. Try a shorter request.") from error
    except APIConnectionError as error:
        raise LLMError(
            "Could not connect to the model server."
        ) from error
    except APIStatusError as error:
        raise LLMError(f"The model server returned an error ({error.status_code}).") from error

    if not response.choices or not response.choices[0].message.content:
        raise LLMError("The model returned an empty response. Try again.")

    return response.choices[0].message.content.strip()