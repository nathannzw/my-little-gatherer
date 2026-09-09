from pydantic import BaseModel, Field


class LLMRequest(BaseModel):
    prompt: str
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)
    top_p: float = Field(default=0.95, gt=0.0, le=1.0)
    max_tokens: int = Field(default=2048, ge=1, le=4096)


class LLMResponse(BaseModel):
    answer: str
    model: str
    elapsed_seconds: float
    prompt_chars: int
    output_chars: int
    finish_reason: str | None
    prompt_tokens: int | None
    completion_tokens: int | None
    total_tokens: int | None
