from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.enums.chat_member_status import ChatMemberStatus
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import database
from misc import logger, bot
import keyboards

router = Router()


@router.callback_query(F.text == 'Что-то')
@logger.catch
async def something(message: Message, state: FSMContext):
    ...
