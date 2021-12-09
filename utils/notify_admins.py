from aiogram import Dispatcher
from loguru import logger

from loader import ADMINS


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            pass
            # await dp.bot.send_message(admin, "Бот Запущен")

        except Exception as err:
            logger.exception(err)
