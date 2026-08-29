import type { ApiError, AskRequest, LLMResult } from "./contracts";

export async function askModel(request: AskRequest): Promise<LLMResult> {
  let response: Response;

  try {
    response = await fetch("/api/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(request),
    });
  } catch {
    throw new Error("Could not connect to the model server.");
  }

  const body = (await response.json()) as ApiError | LLMResult;
  if (!response.ok) {
    throw new Error(body.detail ?? "The model server returned an error.");
  }

  return body as LLMResult;
}