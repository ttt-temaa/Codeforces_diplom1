# Модуль инициализации и запуска Telegram бота.

# Этот модуль отвечает за:
# 1. Создание экземпляра бота
# 2. Настройку диспетчера и хранилища состояний
# 3. Запуск бота


import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from constants import TOKEN

logging.basicConfig(level=logging.INFO)

telegram_bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

import bot.handlers


async def start_bot():
    await dp.start_polling(telegram_bot)
