import asyncio
import logging
import os
import nest_asyncio
from keep_alive import keep_alive
from telegram.ext import Application, CommandHandler

nest_asyncio.apply()

TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

async def start(update, context):
    await update.message.reply_text("سلام ارباب مهراد!")

async def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    keep_alive()
    await app.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
