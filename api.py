from fastapi import FastAPI, Request
from app.utils.validator import UpdateModel
from typing import Optional
from telegram import Update
from app.config.bot import app
from app.config.enviroments import Env



app = FastAPI()


@app.post('/tg-webhook')
async def webhook(request: Request):
    update_data = await request.json()
    telegram_update = Update.de_json(update_data, app.bot)
    await app.process_update(telegram_update)
    return {"status": True}

@app.get('/set-webhook')
async def set_webhook(request: Request):
    secret_key = request.query_params.get('key')
    if not (Env.SECRET_KEY == secret_key):
        return {"status": False, "message": "Invalid Secret Key"}
    result = await app.bot.set_webhook(request.query_params.get('webhook_url'))
    return {"message": "webhook set", "status": False, "result": result}

@app.get('/')
async def index(request: Request):
    return {"bot": "Oprational"}