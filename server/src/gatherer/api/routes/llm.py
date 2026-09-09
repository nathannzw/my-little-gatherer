from fastapi import APIRouter, HTTPException

from gatherer.api.models import LLMRequest, LLMResponse
from gatherer.llm.client import LLMError, ask_llm
from gatherer.llm.prompts.builder import build_messages

router = APIRouter()


@router.post("/ask", response_model=LLMResponse)
def ask(request: LLMRequest) -> LLMResponse:
    try:
        messages = build_messages(
            request.prompt,
            profile="general",
        )
        
        result = ask_llm(
            messages,
            temperature=request.temperature,
            top_p=request.top_p,
            max_tokens=request.max_tokens,
        )
    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error)) from error
    except LLMError as error:
        status_code = 504 if "too long" in str(error) else 502
        raise HTTPException(status_code=status_code, detail=str(error)) from error

    return result