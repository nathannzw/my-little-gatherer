from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from gatherer.api.routes.llm import router as llm_router

app = FastAPI(title="My Little Gatherer API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(llm_router, prefix="/api")