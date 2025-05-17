import React, { useEffect, useState } from "react";

export default function BotConfigForm() {
  const [config, setConfig] = useState<any>(null);

  useEffect(() => {
    fetch("/api/config").then(res => res.json()).then(setConfig);
  }, []);

  const save = () => {
    fetch("/api/config", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(config)
    });
  };

  const start = () => fetch("/api/start", { method: "POST" });
  const stop = () => fetch("/api/stop", { method: "POST" });

  if (!config) return <div>Loading...</div>;

  return (
    <div>
      <h2>Bot Configuration</h2>
      <input value={config.topic} onChange={e => setConfig({ ...config, topic: e.target.value })} />
      <label>
        <input type="checkbox" checked={config.enable_like} onChange={e => setConfig({ ...config, enable_like: e.target.checked })} />
        Like posts
      </label>
      <label>
        <input type="checkbox" checked={config.enable_comment} onChange={e => setConfig({ ...config, enable_comment: e.target.checked })} />
        Comment posts
      </label>
      <label>
        <input type="checkbox" checked={config.enable_add_friend} onChange={e => setConfig({ ...config, enable_add_friend: e.target.checked })} />
        Add friends
      </label>
      <button onClick={save}>Save</button>
      <button onClick={start}>Start</button>
      <button onClick={stop}>Stop</button>
    </div>
  );
}