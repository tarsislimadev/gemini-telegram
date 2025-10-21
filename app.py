from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import google.generativeai as genai
import requests as req

# 

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def aws(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  chat = model.start_chat()
  aws = req.get("https://status.aws.amazon.com/rss/multipleservices-us-east-1.rss")
  chat.send_message(str(aws.text))
  text = chat.send_message('Resume it all in a line.').text
  await update.message.reply_text(text)

async def text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  await update.message.reply_text(f"text: {update.message.message_id}: {update.message.text}")

# 

genai.configure(api_key="<GOOGLE_API_KEY>")

model = genai.GenerativeModel('gemini-2.5-flash')

# 

app = ApplicationBuilder().token("<TELEGRAM_API_KEY>").build()

app.add_handler(CommandHandler("hello", hello))

app.add_handler(CommandHandler("aws", aws))

app.add_handler(MessageHandler(filters.TEXT, text))

app.run_polling()
