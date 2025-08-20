import os
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram.error import NetworkError
import asyncio
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Бот работает с улучшенным соединением!")

if __name__ == "__main__":
    # Настройка улучшенного соединения
    application = Application.builder()\
        .token(TOKEN)\
        .read_timeout(30)\  # Увеличиваем таймаут
        .write_timeout(30)\
        .connect_timeout(30)\
        .pool_timeout(30)\
        .build()
    
    application.add_handler(CommandHandler("start", start))
    
    # Запуск с обработкой ошибок сети
    try:
        print("🟢 Запуск бота с улучшенными настройками сети...")
        application.run_polling(
            poll_interval=1.0,
            timeout=30,
            drop_pending_updates=True
        )
    except NetworkError as e:
        print(f"🔴 Сетевая ошибка: {e}")
    except Exception as e:
        print(f"🔴 Общая ошибка: {e}")
    