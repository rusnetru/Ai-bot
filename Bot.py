import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("/start executed")  # Логирование
    await update.message.reply_text("🚀 Бот работает!")

if __name__ == "__main__":
    print("=== INIT BOT ===")
    try:
        app = Application.builder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        print("=== POLLING START ===")
        app.run_polling()
    except Exception as e:
        print(f"!!! FATAL ERROR: {e}")
        raise