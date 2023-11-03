import os

from loguru import logger
from aiogram import Bot


logger.add(
    'logs/log.log',
    format='{time:HH:mm:ss} {level} {message}',
    level='DEBUG',
    rotation='50 MB'
)

bot = Bot(token=os.getenv('BOT_TOKEN'))
