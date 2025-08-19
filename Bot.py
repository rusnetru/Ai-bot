import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("/start executed!")  # Проверьте в логах Railway
    await update.message.reply_text("🟢 Бот работает!")

if __name__ == "__main__":
    print("=== БОТ ЗАПУЩЕН ===")  # Должно быть в логах
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()