import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram.error import NetworkError
import requests
import asyncio

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Бот работает!")

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        url = f"https://newsapi.org/v2/top-headlines?country=us&pageSize=3&apiKey={NEWS_API_KEY}"
        response = requests.get(url, timeout=10).json()
        
        if response.get("articles"):
            for article in response["articles"][:3]:
                await update.message.reply_text(
                    f"📰 *{article['title']}*\n\n{article['url']}",
                    parse_mode="Markdown"
                )
    except:
        await update.message.reply_text("📭 Новости временно недоступны")

if __name__ == "__main__":
    print("🚀 Запуск бота...")
    
    # Настройка с улучшенными таймаутами
    app = Application.builder()\
        .token(TELEGRAM_TOKEN)\
        .read_timeout(30)\
        .write_timeout(30)\
        .connect_timeout(30)\
        .build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("news", news))
    
    # Запуск с обработкой ошибок
    try:
        app.run_polling(
            poll_interval=1.0,
            timeout=30,
            drop_pending_updates=True
        )
    except NetworkError:
        print("🔁 Перезапуск из-за сетевой ошибки")
    except Exception as e:
        print(f"🔴 Ошибка: {e}")