import type { LLMResult } from "@/lib/contracts";

export function RequestLog({ result }: { result: LLMResult | null }) {
  return (
    <section className="request-log" aria-labelledby="request-log-title">
      <div className="log-heading">
        <h2 id="request-log-title">Last request</h2>
        <span>LOG</span>
      </div>
      {!result ? (
        <p className="muted">No completed request yet.</p>
      ) : (
        <dl>
          <div><dt>Model</dt><dd>{result.model}</dd></div>
          <div><dt>Response time</dt><dd>{result.elapsed_seconds.toFixed(1)} s</dd></div>
          <div><dt>Output</dt><dd>{result.output_chars.toLocaleString()} chars</dd></div>
          <div><dt>Finish reason</dt><dd>{result.finish_reason ?? "unknown"}</dd></div>
          <div><dt>Prompt</dt><dd>{result.prompt_chars.toLocaleString()} chars</dd></div>
          <div className="wide-row"><dt>Token usage</dt><dd>{result.total_tokens !== null ? `${(result.prompt_tokens ?? 0).toLocaleString()} prompt + ${(result.completion_tokens ?? 0).toLocaleString()} output = ${result.total_tokens.toLocaleString()} total` : "Not provided by model server"}</dd></div>
        </dl>
      )}
    </section>
  );
}