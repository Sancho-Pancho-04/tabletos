import telebot
import time
import os
from datetime import datetime, timedelta
import threading

TOKEN = os.environ.get("8641202785:AAGDzpqE2HsIE6WjO-iA2RL5U2fjDa-O4e8
")
if not TOKEN:
    print("❌ Ошибка: TELEGRAM_TOKEN не найден в переменных окружения")
    exit(1)

bot = telebot.TeleBot(TOKEN)

# Удаляем вебхук и ждем
bot.remove_webhook()
time.sleep(1)  # Небольшая пауза

CHAT_ID = 123456789
last_sent_date = None

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "✅ Бот запущен! Буду напоминать о таблетос каждый день в 21:00")

def send_pill():
    bot.send_message(CHAT_ID, "💊 таблетос 💊")
    print(f"💊 Отправлено в {datetime.now().strftime('%H:%M:%S')}")

def reminder_loop():
    global last_sent_date
    while True:
        now = datetime.now()
        target = now.replace(hour=21, minute=0, second=0, microsecond=0)
        
        if now >= target:
            target += timedelta(days=1)
        
        wait_seconds = (target - now).total_seconds()
        time.sleep(wait_seconds)
        
        current_date = datetime.now().date()
        if last_sent_date != current_date:
            send_pill()
            last_sent_date = current_date
        
        time.sleep(60)

threading.Thread(target=reminder_loop, daemon=True).start()

if __name__ == "__main__":
    print("🤖 Бот запущен")
    
    # Запускаем с увеличенным таймаутом
    bot.infinity_polling(timeout=60, long_polling_timeout=60)
