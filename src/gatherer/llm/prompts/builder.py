from collections.abc import Sequence
from typing import TypedDict

from .defaults import SYSTEM_PROMPTS


class ChatMessage(TypedDict):
    role: str
    content: str


def build_messages(
    user_input: str,
    *,
    profile: str = "general",
    history: Sequence[ChatMessage] | None = None,
) -> list[ChatMessage]:
    user_input = user_input.strip()

    if not user_input:
        raise ValueError("Please enter a question before sending it.")

    try:
        system_prompt = SYSTEM_PROMPTS[profile]
    except KeyError as error:
        raise ValueError(f"Unknown prompt profile: {profile}") from error

    messages: list[ChatMessage] = [
        {"role": "system", "content": system_prompt},
    ]

    if history:
        messages.extend(history)

    messages.append({"role": "user", "content": user_input})

    return messages