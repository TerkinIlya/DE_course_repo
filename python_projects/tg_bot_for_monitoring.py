import psutil
import requests
import time
from dotenv import load_dotenv
from os import getenv

load_dotenv()

bot_token = getenv('BOT_TOKEN')
chat_id = getenv('CHAT_ID')


# Функция для отправки сообщения в Telegram
def send_telegram_alert(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML"
    }
    response = requests.post(url, data=payload)
    return response


# Пороговое значение для загрузки CPU (в процентах)
cpu_threshold = 15

while True:
    # Получаем загрузку CPU
    cpu_usage = psutil.cpu_percent(interval=1)
    print(cpu_usage)
    # Проверяем, превышает ли загрузка CPU пороговое значение
    if cpu_usage > cpu_threshold:
        message = f"Внимание! Высокая загрузка CPU: {cpu_usage}%"
        response = send_telegram_alert(bot_token, chat_id, message)

        if response.status_code == 200:
            print("Алерт успешно отправлен!")
        else:
            print(f"Ошибка отправки алерта: {response.status_code}")

    # Пауза перед следующим измерением (например, 60 секунд)
    time.sleep(5)
