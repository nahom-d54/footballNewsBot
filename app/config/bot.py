from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from ..controllers import commands
from .enviroments import Env

app = ApplicationBuilder().token(Env.TELEGRAM_BOT_TOKEN).build()
app.add_handlers(commands)