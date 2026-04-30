import telebot
import time
from datetime import datetime
import threading

bot = telebot.TeleBot("8641202785:AAGDzpqE2HsIE6WjO-iA2RL5U2fjDa-O4e8")

CHAT_ID = None
last_sent_date = None  # Запоминаем дату последней отправки


@bot.message_handler(commands=['start'])
def start(message):
    global CHAT_ID
    CHAT_ID = message.chat.id
    bot.send_message(CHAT_ID, "✅ Бот запущен! Буду отправлять 'таблетос' каждый день в 21:00")


def send_pill_reminder():
    """Отправляет сообщение"""
    global last_sent_date
    if CHAT_ID:
        bot.send_message(CHAT_ID, "💊 таблетос 💊")
        last_sent_date = datetime.now().date()  # Запоминаем, что сегодня уже отправили


def check_time():
    """Проверяет время и отправляет сообщение в 21:00"""
    global last_sent_date

    while True:
        now = datetime.now()
        today = now.date()

        # Проверяем: время 21:00 И сегодня еще не отправляли
        if now.hour == 21 and now.minute == 0 and last_sent_date != today:
            send_pill_reminder()

        # Проверяем каждые 30 секунд (реже, чтобы меньше нагружать)
        time.sleep(30)


# Запускаем проверку времени в отдельном потоке
def start_checker():
    thread = threading.Thread(target=check_time, daemon=True)
    thread.start()


if __name__ == '__main__':
    print("Бот запущен...")
    start_checker()
    bot.infinity_polling()