from loguru import logger
from aiogram.utils.exceptions import TelegramAPIError

from loader import dp


@dp.errors_handler()
async def errors_handler(update, exception):
    """
    Exceptions handler. Catches all exceptions within task factory tasks.
    :param dispatcher:
    :param update:
    :param exception:
    :return: stdout logging
    """
    if isinstance(exception, TelegramAPIError):
        logger.exception(f'TelegramAPIError: {exception} \nUpdate: {update}')
        return True

    logger.exception(f'Update: {update} \n{exception}')
