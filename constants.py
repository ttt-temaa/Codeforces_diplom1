# Модуль констант и конфигурации приложения.

# Этот модуль содержит:
# 1. Настройки подключения к базе данных
# 2. Настройки временной зоны для планировщика
# 3. Токен Telegram бота


import os

from dotenv import load_dotenv
from pytz import timezone

load_dotenv()

DB_USER = os.getenv("DB_USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DATABASE = os.getenv("DATABASE")

# Настройки временной зоны для планировщика задач
moscow = timezone('Europe/Moscow')  # Временная зона Москвы

# Настройки Telegram бота
TOKEN = os.getenv("TOKEN")  # Токен бота
