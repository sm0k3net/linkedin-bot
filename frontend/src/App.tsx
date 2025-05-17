import React, { useEffect, useState } from "react";
import BotConfigForm from "./BotConfigForm";
import LogViewer from "./LogViewer";

function App() {
  const [status, setStatus] = useState<{ running: boolean }>({ running: false });

  useEffect(() => {
    fetch("/api/status").then(res => res.json()).then(setStatus);
  }, []);

  return (
    <div style={{ fontFamily: "sans-serif", maxWidth: 600, margin: "auto" }}>
      <h1>LinkedIn Bot Dashboard</h1>
      <div>
        <b>Status:</b> {status.running ? "🟢 Running" : "🔴 Stopped"}
      </div>
      <BotConfigForm />
      <LogViewer />
    </div>
  );
}

export default App;