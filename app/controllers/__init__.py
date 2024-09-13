from .commands import *
from telegram.ext import ApplicationBuilder, CommandHandler

command_list = ['start', 'check']

commands = [CommandHandler('start', start), CommandHandler('check', check_now)]