import threading, time
from .config import load_config
from .logger import log_action
from .deepseek import generate_comment

_bot_thread = None
_bot_running = False

def _bot_loop():
    config = load_config()
    log_action("Bot started", "info")
    while _bot_running:
        # Здесь эмулируем действия: лайк, коммент, добавление в друзья
        log_action("Searching for posts...", "info")
        # ... эмуляция поиска ...
        post = {"id": 1, "text": "AI is changing the world"}
        if config.enable_like:
            log_action(f"Liking post {post['id']}", "like")
        if config.enable_comment:
            comment = generate_comment(config.topic, post["text"])
            log_action(f"Commented: {comment}", "comment")
        if config.enable_add_friend:
            log_action("Sent friend request", "add_friend")
        time.sleep(config.action_delay)
    log_action("Bot stopped", "info")

def start_bot():
    global _bot_thread, _bot_running
    if _bot_running:
        return
    _bot_running = True
    _bot_thread = threading.Thread(target=_bot_loop, daemon=True)
    _bot_thread.start()

def stop_bot():
    global _bot_running
    _bot_running = False

def bot_status():
    return {"running": _bot_running}