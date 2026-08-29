from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from gatherer.llm.client import LLMError, LLMResult, ask_llm

router = APIRouter()


class AskRequest(BaseModel):
    prompt: str
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)
    top_p: float = Field(default=0.95, gt=0.0, le=1.0)
    max_tokens: int = Field(default=2048, ge=1, le=4096)


class AskResponse(BaseModel):
    answer: str
    model: str
    elapsed_seconds: float
    prompt_chars: int
    output_chars: int
    finish_reason: str | None
    prompt_tokens: int | None
    completion_tokens: int | None
    total_tokens: int | None

    @classmethod
    def from_result(cls, result: LLMResult) -> "AskResponse":
        return cls(**result.__dict__)


@router.post("/ask", response_model=AskResponse)
def ask(request: AskRequest) -> AskResponse:
    try:
        result = ask_llm(
            request.prompt,
            temperature=request.temperature,
            top_p=request.top_p,
            max_tokens=request.max_tokens,
        )
    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error)) from error
    except LLMError as error:
        status_code = 504 if "too long" in str(error) else 502
        raise HTTPException(status_code=status_code, detail=str(error)) from error

    return AskResponse.from_result(result)