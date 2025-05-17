from pydantic import BaseModel
import json, os

CONFIG_PATH = "bot_config.json"

class BotConfig(BaseModel):
    topic: str = "AI"
    scenario: str = "like_and_comment"
    enable_like: bool = True
    enable_comment: bool = True
    enable_add_friend: bool = False
    action_delay: int = 30  # seconds

def load_config() -> BotConfig:
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as f:
            return BotConfig(**json.load(f))
    return BotConfig()

def save_config(config: BotConfig):
    with open(CONFIG_PATH, "w") as f:
        json.dump(config.dict(), f, indent=2)