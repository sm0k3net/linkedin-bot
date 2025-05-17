import React, { useEffect, useState } from "react";

export default function LogViewer() {
  const [logs, setLogs] = useState<any[]>([]);

  useEffect(() => {
    const interval = setInterval(() => {
      fetch("/api/logs").then(res => res.json()).then(setLogs);
    }, 2000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div>
      <h2>Bot Logs</h2>
      <div style={{ maxHeight: 200, overflow: "auto", background: "#eee", padding: 10 }}>
        {logs.map((log, i) => (
          <div key={i}>
            <b>{log.timestamp}</b> [{log.action}]: {log.message}
          </div>
        ))}
      </div>
    </div>
  );
}