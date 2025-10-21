from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import google.generativeai as genai
import requests as req
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-2.5-flash')

async def gemini(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  chat = model.start_chat()
  await update.message.reply_text(chat.send_message(str(update.message.text)).text)

async def text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  await update.message.reply_text(f"text: {update.message.message_id}: {update.message.text}")

app = ApplicationBuilder().token(os.getenv("TELEGRAM_API_KEY")).build()

app.add_handler(CommandHandler("gemini", gemini))

app.add_handler(MessageHandler(filters.TEXT, text))

app.run_polling()
