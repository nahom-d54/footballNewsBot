from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from ..utils.feed import feed_parser
from ..utils.date_parser import date_stringify
from ..config.enviroments import Env


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello!")

async def check_now(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("checkig now")
    url = "https://www.90min.com/posts.rss"
    feeds = feed_parser(url)

    
    for feed in feeds:
        html_formatting = f"""
<b>{feed['title']}</b>

<blockquote expandable>{feed['description']}</blockquote>

Date: <i>{date_stringify(feed['pubDate'])}</i>
    """ 
        await context.bot.send_photo(chat_id=Env.CHANNEL_ID,caption=html_formatting, parse_mode='html', photo=feed['media'])
