from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from src.misc import logger

router = Router()


@router.callback_query(F.text == 'Что-то')
@logger.catch
async def something(message: Message, state: FSMContext):
    ...
