from app.config.bot import app
from dotenv import load_dotenv
from app.config.enviroments import Env

load_dotenv()


def delete_webhook():
    app.bot.delete_webhook()

def set_webhook(url: str):
    # set secret token
    app.bot.set_webhook(url)
def main():
    if Env.CURRENT_ENV == 'prod':
        app.run_webhook()
    else:
        app.run_polling()
        
if __name__ == "__main__":
    print("main",Env.TELEGRAM_BOT_TOKEN)

    main()