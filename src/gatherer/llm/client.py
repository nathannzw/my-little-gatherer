from openai import OpenAI

from gatherer.core.config import settings


client = OpenAI(
    base_url=settings.llm_url,
    api_key="not-required"
)


def ask_llm(prompt: str) -> str:

    response = client.chat.completions.create(
        model=settings.model_name,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content