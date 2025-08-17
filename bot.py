import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import requests

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот для новостей. Напиши /news")

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
        response = requests.get(url).json()
        if response.get("articles"):
            for article in response["articles"][:3]:  # Уменьшил до 3 новостей
                await update.message.reply_text(
                    f"📌 *{article['title']}*\n\n{article['url']}",
                    parse_mode="Markdown"
                )
        else:
            await update.message.reply_text("🔴 Не удалось получить новости")
    except Exception as e:
        await update.message.reply_text("⚠️ Ошибка при запросе новостей")
        print(f"NewsAPI Error: {e}")  # Логируем ошибку

if __name__ == "__main__":
    try:
        print("🟢 Бот запускается...")
        app = Application.builder().token(TELEGRAM_TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("news", news))
        print("🟢 Обработчики зарегистрированы")
        app.run_polling()
    except Exception as e:
        print(f"🔴 Критическая ошибка: {e}")
        raise  # Чтобы увидеть полную трассировку ошибки
