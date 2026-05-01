import telebot
import time
import os
from datetime import datetime, timedelta

# ✅ ВСТАВЬТЕ ТОКЕН НАПРЯМУЮ (только для теста!)
TOKEN = "8641202785:AAGDzpqE2HsIE6WjO-iA2RL5U2fjDa-O4e8"
bot = telebot.TeleBot(TOKEN)

CHAT_ID = None

@bot.message_handler(commands=['start'])
def start(message):
    global CHAT_ID
    CHAT_ID = message.chat.id
    bot.reply_to(message, "✅ Бот запущен! Таблетос в 21:00")
    print(f"✅ Пользователь {CHAT_ID} запустил бота")

def send_pill():
    if CHAT_ID:
        bot.send_message(CHAT_ID, "💊 таблетос 💊")
        print(f"💊 Отправлено в {datetime.now().strftime('%H:%M:%S')}")

if __name__ == "__main__":
    print("🤖 Бот запущен")
    
    import threading
    threading.Thread(target=bot.infinity_polling, daemon=True).start()
    
    last_sent = None
    while True:
        now = datetime.now()
        if now.hour == 21 and now.minute == 0 and last_sent != now.date():
            send_pill()
            last_sent = now.date()
        time.sleep(30)
