export type GenerationSettings = {
  temperature: number;
  top_p: number;
  max_tokens: number;
};

export type AskRequest = GenerationSettings & {
  prompt: string;
};

export type LLMResult = {
  answer: string;
  model: string;
  elapsed_seconds: number;
  prompt_chars: number;
  output_chars: number;
  finish_reason: string | null;
  prompt_tokens: number | null;
  completion_tokens: number | null;
  total_tokens: number | null;
};

export type ApiError = {
  detail?: string;
};