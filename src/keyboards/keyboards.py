from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='👤 Профиль', callback_data='профиль')],
        [InlineKeyboardButton(text='🛒 Сделать заказ', callback_data='сделать заказ'),
         InlineKeyboardButton(text='📋 Мои заказы', callback_data='мои заказы')],
        [InlineKeyboardButton(text='➕ Добавить чат', callback_data='добавить чат'),
         InlineKeyboardButton(text='📋Список чатов', callback_data='список чатов')]
    ])
