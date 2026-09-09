"use client";

import { FormEvent, useState } from "react";
import { askModel } from "@/lib/api";
import type { GenerationSettings, LLMResult } from "@/lib/contracts";
import { GenerationSettingsPanel } from "./generation/GenerationSettingsPanel";
import { RequestLog } from "./request-log/RequestLog";

const defaultSettings: GenerationSettings = {
  temperature: 0.7,
  top_p: 0.95,
  max_tokens: 2048,
};

export function GathererWorkspace() {
  const [prompt, setPrompt] = useState("");
  const [settings, setSettings] = useState(defaultSettings);
  const [result, setResult] = useState<LLMResult | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setError(null);
    setIsLoading(true);

    try {
      const nextResult = await askModel({ prompt, ...settings });
      setResult(nextResult);
    } catch (requestError) {
      setError(
        requestError instanceof Error
          ? requestError.message
          : "The request could not be completed.",
      );
    } finally {
      setIsLoading(false);
    }
  }

  return (
    <main className="page-shell">
      <header className="site-header">
        <div>
          <p className="eyebrow">Local intelligence workspace</p>
          <h1>My Little Gatherer</h1>
        </div>
        <span className="status-dot"><span /> llama.cpp ready to query</span>
      </header>

      <div className="workspace-grid">
        <section className="question-panel" aria-labelledby="question-title">
          <div className="section-heading">
            <div>
              <p className="section-kicker">01 / Ask</p>
              <h2 id="question-title">What are you curious about?</h2>
            </div>
            <span className="model-chip">ONE SHOT</span>
          </div>

          <form onSubmit={handleSubmit}>
            <label htmlFor="question">Question</label>
            <textarea
              id="question"
              value={prompt}
              onChange={(event) => setPrompt(event.target.value)}
              placeholder="Ask the local model something..."
              maxLength={10000}
              rows={7}
            />
            <div className="form-footer">
              <span className="character-count">{prompt.length.toLocaleString()} / 10,000</span>
              <button type="submit" disabled={isLoading}>
                {isLoading ? "Thinking..." : "Ask model"}
                <span aria-hidden="true">{isLoading ? "..." : "->"}</span>
              </button>
            </div>
          </form>

          {error && <p className="message error-message" role="alert">{error}</p>}

          {result && (
            <article className="answer-block" aria-live="polite">
              <div className="answer-label"><span /> Answer</div>
              <p>{result.answer}</p>
            </article>
          )}
        </section>

        <aside className="sidebar">
          <GenerationSettingsPanel settings={settings} onChange={setSettings} />
          <RequestLog result={result} />
        </aside>
      </div>
    </main>
  );
}