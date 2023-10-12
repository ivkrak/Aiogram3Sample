import asyncio

from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import start, admins
from misc import bot, logger


# Запуск бота
async def main():
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(
        start.router,
        admins.router
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logger.info('Бот запущен')
    asyncio.run(main())
