import datetime
from .models import ActionLog

LOG_PATH = "bot_log.json"

def log_action(message: str, action_type: str):
    log = ActionLog(
        timestamp=datetime.datetime.now().isoformat(),
        action=action_type,
        message=message
    )
    logs = get_logs()
    logs.append(log)
    with open(LOG_PATH, "w") as f:
        f.write("[" + ",".join([l.json() for l in logs]) + "]")

def get_logs():
    try:
        with open(LOG_PATH, "r") as f:
            import json
            return [ActionLog(**x) for x in json.load(f)]
    except Exception:
        return []