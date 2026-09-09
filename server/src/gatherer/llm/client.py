import time
from collections.abc import Sequence

from openai import OpenAI
from openai import APIConnectionError, APIStatusError, APITimeoutError

from gatherer.api.models import LLMResponse
from gatherer.core.config import settings
from gatherer.llm.prompts.builder import ChatMessage


class LLMError(RuntimeError):
    """An expected failure while communicating with the model server."""


client = OpenAI(
    base_url=settings.llm_url,
    api_key="not-required",
    timeout=60.0,
)


def ask_llm(
    messages: Sequence[ChatMessage],
    *,
    temperature: float = 0.7,
    top_p: float = 0.95,
    max_tokens: int = 512,
) -> LLMResponse:
    messages = list(messages)

    if not messages:
        raise ValueError("At least one message is required.")

    prompt_text = "\n".join(
        message["content"]
        for message in messages
        if message["role"] == "user"
    )

    if len(prompt_text) > 10_000:
        raise ValueError("Please keep your question under 10,000 characters.")
    
    if not 0.0 <= temperature <= 2.0:
        raise ValueError("Temperature must be between 0 and 2.")
    if not 0.0 < top_p <= 1.0:
        raise ValueError("Top-p must be greater than 0 and no more than 1.")
    if not 1 <= max_tokens <= 4_096:
        raise ValueError("Maximum output tokens must be between 1 and 4,096.")

    started_at = time.perf_counter()

    try:
        response = client.chat.completions.create(
            model=settings.model_name,
            messages=messages,
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

    answer = response.choices[0].message.content.strip()
    elapsed_seconds = time.perf_counter() - started_at
    usage = response.usage
    choice = response.choices[0]

    return LLMResponse(
        answer=answer,
        model=response.model,
        elapsed_seconds=elapsed_seconds,
        prompt_chars=len(prompt_text),
        output_chars=len(answer),
        finish_reason=choice.finish_reason,
        prompt_tokens=getattr(usage, "prompt_tokens", None),
        completion_tokens=getattr(usage, "completion_tokens", None),
        total_tokens=getattr(usage, "total_tokens", None),
    )