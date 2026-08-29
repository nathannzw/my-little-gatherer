import type { GenerationSettings } from "@/lib/contracts";

type Props = {
  settings: GenerationSettings;
  onChange: (settings: GenerationSettings) => void;
};

export function GenerationSettingsPanel({ settings, onChange }: Props) {
  function update(key: keyof GenerationSettings, value: number) {
    onChange({ ...settings, [key]: value });
  }

  return (
    <section className="settings-panel" aria-labelledby="settings-title">
      <div className="section-heading compact">
        <div>
          <p className="section-kicker">Controls</p>
          <h2 id="settings-title">Generation settings</h2>
        </div>
        <span className="settings-mark">///</span>
      </div>

      <label className="range-label" htmlFor="temperature">
        <span>Temperature <output>{settings.temperature.toFixed(1)}</output></span>
        <input id="temperature" type="range" min="0" max="2" step="0.1" value={settings.temperature} onChange={(event) => update("temperature", Number(event.target.value))} />
      </label>
      <label className="range-label" htmlFor="top-p">
        <span>Top-p <output>{settings.top_p.toFixed(2)}</output></span>
        <input id="top-p" type="range" min="0.01" max="1" step="0.01" value={settings.top_p} onChange={(event) => update("top_p", Number(event.target.value))} />
      </label>
      <label className="number-label" htmlFor="max-tokens">
        <span>Maximum output tokens</span>
        <input id="max-tokens" type="number" min="1" max="4096" step="1" value={settings.max_tokens} onChange={(event) => update("max_tokens", Number(event.target.value))} />
      </label>

      <details>
        <summary>What should I use?</summary>
        <p>Temperature controls predictability. Top-p limits the probability pool. Maximum output tokens controls response length.</p>
        <p>Good starting point: <strong>0.7</strong> temperature, <strong>0.95</strong> top-p, and <strong>2048</strong> tokens.</p>
      </details>
    </section>
  );
}