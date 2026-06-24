import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Main live hoon 🚀")

app = ApplicationBuilder().token(os.environ.get("BOT_TOKEN")).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
