from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from misc import logger

router = Router()


@router.message(Command('start'), F.text)
@logger.catch
async def start(message: Message):
    await message.answer(
        text='Привет, я шаблон'
    )
