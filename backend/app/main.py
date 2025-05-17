from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from .config import BotConfig, load_config, save_config
from .bot import start_bot, stop_bot, bot_status
from .logger import get_logs
from .models import ActionLog, BotStatus
from typing import List

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/status", response_model=BotStatus)
def status():
    return bot_status()

@app.post("/start")
def start(background_tasks: BackgroundTasks):
    background_tasks.add_task(start_bot)
    return {"status": "starting"}

@app.post("/stop")
def stop():
    stop_bot()
    return {"status": "stopped"}

@app.get("/config", response_model=BotConfig)
def get_config():
    return load_config()

@app.post("/config")
def set_config(config: BotConfig):
    save_config(config)
    return {"status": "saved"}

@app.get("/logs", response_model=List[ActionLog])
def logs():
    return get_logs()