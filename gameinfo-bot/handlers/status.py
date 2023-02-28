from telegram import Update 
from telegram.ext import ContextTypes

import message_texts
from modules.API import *

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
	game = update.message.text.lower()
	
	rq = GameInfo(game)
	print(rq.get_status())

	await update.message.reply_text(text=message_texts.STATUS)