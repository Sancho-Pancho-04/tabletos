import telebot
import time
import os
from datetime import datetime, timedelta

TOKEN = os.environ.get("8641202785:AAGDzpqE2HsIE6WjO-iA2RL5U2fjDa-O4e8")
bot = telebot.TeleBot(TOKEN)

CHAT_ID = 123456789  # ВСТАВЬТЕ ВАШ ID

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "✅ Бот запущен! Таблетос в 21:00")

def send_pill():
    bot.send_message(CHAT_ID, "💊 таблетос 💊")

if __name__ == "__main__":
    print("Бот запущен")
    
    # Запускаем бота в фоне
    import threading
    threading.Thread(target=bot.infinity_polling, daemon=True).start()
    
    # Основной цикл
    last_sent = None
    while True:
        now = datetime.now()
        if now.hour == 21 and now.minute == 0 and last_sent != now.date():
            send_pill()
            last_sent = now.date()
        time.sleep(30)
