import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import requests

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")  # Ваш токен Telegram Bot
NEWS_API_KEY = os.getenv("NEWS_API_KEY")      # Ваш ключ от NewsAPI

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот для новостей. Напиши /news")

# Команда /news — присылает 5 новостей
async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🛠 Новости временно недоступны")
    print("Запрос /news получен")  # Логируем факт вызова

# async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     url = f"https://newsapi.org/v2/top-headlines?country=ru&apiKey={NEWS_API_KEY}"
#     response = requests.get(url).json()
#     if response.get("articles"):
#         for article in response["articles"][:5]:
#             await update.message.reply_text(
#                 f"📌 *{article['title']}*\n\n{article['url']}",
#                 parse_mode="Markdown"
#             )
#     else:
#         await update.message.reply_text("Не удалось получить новости. Проверьте API-ключ.")

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
        raise  # Это поможет увидеть ошибку в логах
