from fastapi import FastAPI, Request, Response
from http import HTTPStatus
from telegram import Update
from app.config.bot import app as bot_app
from app.config.enviroments import Env
import logging
from contextlib import asynccontextmanager


logging.basicConfig(level=logging.INFO)


    
@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("Initializing PTB application...")
    if not bot_app._initialized:
        await bot_app.initialize()

    logging.info("PTB application initialized.")
    yield

    
    logging.info("Shutting down PTB application...")
    await bot_app.shutdown()
    logging.info("PTB application shut down.")
    
    
app = FastAPI(lifespan=lifespan)


@app.post('/tg-webhook')
async def webhook(request: Request):
    if not bot_app._initialized:
        await bot_app.initialize()
    update_data = await request.json()
    logging.info("Update: ")
    logging.info(update_data)
    telegram_update = Update.de_json(update_data, bot_app.bot)
    await bot_app.process_update(telegram_update)
    return Response({"status": True}, status_code=HTTPStatus.OK)

@app.get('/set-webhook')
async def set_webhook(request: Request):
    secret_key = request.query_params.get('key')
    if not (Env.SECRET_KEY == secret_key):
        return {"status": False, "message": "Invalid Secret Key"}
    await bot_app.bot.delete_webhook()
    result = await bot_app.bot.set_webhook(request.query_params.get('webhook_url'))
    logging.info(result)
    return {"message": "webhook set", "status": True, "result": result}

@app.get('/')
async def index(request: Request):
    return {"bot": "Oprational"}