from fastapi import FastAPI, Request
from telegram import Update
from app.config.bot import app as bot_app
from app.config.enviroments import Env
import logging
from contextlib import asynccontextmanager



logger = logging.Logger("Bot logger")


    
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize the PTB application during FastAPI startup
    await bot_app.initialize()
    
    # Yield control to the app
    yield
    
    # Gracefully shut down PTB application during FastAPI shutdown
    await bot_app.shutdown()
    
app = FastAPI(lifespan=lifespan)


@app.post('/tg-webhook')
async def webhook(request: Request):
    update_data = await request.json()
    logger.info("Update: ")
    logger.info(update_data)
    telegram_update = Update.de_json(update_data, bot_app.bot)
    await bot_app.process_update(telegram_update)
    return {"status": True}

@app.get('/set-webhook')
async def set_webhook(request: Request):
    secret_key = request.query_params.get('key')
    if not (Env.SECRET_KEY == secret_key):
        return {"status": False, "message": "Invalid Secret Key"}
    result = await bot_app.bot.set_webhook(request.query_params.get('webhook_url'))
    logger.info(result)
    return {"message": "webhook set", "status": True, "result": result}

@app.get('/')
async def index(request: Request):
    return {"bot": "Oprational"}