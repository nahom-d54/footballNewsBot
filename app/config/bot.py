from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, Application
from ..controllers import commands
from .enviroments import Env

#app = ApplicationBuilder().token(Env.TELEGRAM_BOT_TOKEN).build()
app = (
    Application.builder()
    .updater(None)
    .token(Env.TELEGRAM_BOT_TOKEN) # replace <your-bot-token>
    .read_timeout(7)
    .get_updates_read_timeout(42)
    .build()
    )
app.add_handlers(commands)