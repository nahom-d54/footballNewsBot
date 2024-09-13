import os

class Env:
    TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "6383844976:AAE9-7CgGs9oeBDJuK71vEb3sF5DodiQZKA")
    WEBHOOK_URL = os.environ.get("WEBHOOK_URL")
    CURRENT_ENV = os.environ.get('CURRENT_ENV', 'dev') # dev, prod
    CHANNEL_ID = os.environ.get("CHANNEL_ID", "-1002249060885")
    SECRET_KEY = os.environ.get('SECRET_KEY',"insecure-secret-key")
    