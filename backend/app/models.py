from pydantic import BaseModel

class ActionLog(BaseModel):
    timestamp: str
    action: str
    message: str

class BotStatus(BaseModel):
    running: bool