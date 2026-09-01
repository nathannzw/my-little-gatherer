"use client";

import { FormEvent, useRef, useState } from "react";
import { askModel } from "@/lib/api";
import type { GenerationSettings, LLMResult } from "@/lib/contracts";
import { GenerationSettingsPanel } from "./generation/GenerationSettingsPanel";
import { RequestLog } from "./request-log/RequestLog";
import { Message, MessageContent } from "@/components/ui/message";
import { Bubble, BubbleContent } from "@/components/ui/bubble";
import {
  MessageScroller,
  MessageScrollerButton,
  MessageScrollerContent,
  MessageScrollerItem,
  MessageScrollerProvider,
  MessageScrollerViewport,
} from "@/components/ui/message-scroller";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { SendIcon } from "lucide-react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

const defaultSettings: GenerationSettings = {
  temperature: 0.7,
  top_p: 0.95,
  max_tokens: 2048,
};

type ChatMessage = {
  id: string;
  role: "user" | "assistant" | "error";
  content: string;
}

export function GathererWorkspace() {
  const [prompt, setPrompt] = useState("");
  const [settings, setSettings] = useState(defaultSettings);
  const [result, setResult] = useState<LLMResult | null>(null);
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [error, setError] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const idCounter = useRef(0);

 function nextId() {
    idCounter.current += 1;
    return `msg-${idCounter.current}`;
  }

   async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const trimmed = prompt.trim();
    if (!trimmed || isLoading) return;

    setMessages((prev) => [...prev, { id: nextId(), role: "user", content: trimmed }]);
    setPrompt("");
    setIsLoading(true);

    try {
      const nextResult = await askModel({ prompt: trimmed, ...settings });
      setResult(nextResult);
      setMessages((prev) => [
        ...prev,
        { id: nextId(), role: "assistant", content: nextResult.answer },
      ]);
    } catch (requestError) {
      const messageText =
        requestError instanceof Error
          ? requestError.message
          : "The request could not be completed.";
      setMessages((prev) => [...prev, { id: nextId(), role: "error", content: messageText }]);
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

         <MessageScrollerProvider>
            <MessageScroller className="h-[420px] rounded-lg border bg-muted">
              <MessageScrollerViewport>
                <MessageScrollerContent className="flex flex-col gap-2 p-4">
                  {messages.length === 0 && (
                    <p className="text-sm text-muted-foreground">
                      Ask little gatherer something 🌱
                    </p>
                  )}
                  {messages.map((message) => (
                    <MessageScrollerItem
                      key={message.id}
                      messageId={message.id}
                      scrollAnchor={message.role === "user"}
                      className="pb-3"
                    >
                      {message.role === "error" ? (
                        <p className="message error-message" role="alert">
                          {message.content}
                        </p>
                      ) : (
                        <Message align={message.role === "user" ? "end" : "start"}>
                          <MessageContent>
                            <Bubble variant={message.role === "user" ? "tinted" : "secondary"}>
                              <BubbleContent>
                                <ReactMarkdown remarkPlugins={[remarkGfm]}>{message.content}</ReactMarkdown>
                              </BubbleContent>
                            </Bubble>
                          </MessageContent>
                        </Message>
                      )}
                    </MessageScrollerItem>
                  ))}
                  {isLoading && (
                    <Message align="start">
                      <MessageContent>
                        <Bubble variant="secondary">
                          <BubbleContent>Thinking...</BubbleContent>
                        </Bubble>
                      </MessageContent>
                    </Message>
                  )}
                </MessageScrollerContent>
              </MessageScrollerViewport>
              <MessageScrollerButton className="text-primary hover:text-primary/70" />
            </MessageScroller>
          </MessageScrollerProvider>

          <form onSubmit={handleSubmit} className="mt-3 flex items-center gap-2">
            <Input
              value={prompt}
              onChange={(event) => setPrompt(event.target.value)}
              placeholder="Ready to gather..."
              maxLength={10000}
              aria-label="Question"
              disabled={isLoading}
            />
            <Button type="submit" disabled={isLoading || !prompt.trim()} size="icon" className="w-auto px-3" aria-label="Send">
              <SendIcon />
            </Button>
          </form>
        </section>

        <aside className="sidebar">
          <GenerationSettingsPanel settings={settings} onChange={setSettings} />
          <RequestLog result={result} />
        </aside>
      </div>
    </main>
  );
}