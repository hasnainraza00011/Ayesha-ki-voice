
from handlers.startup import setup_handlers
from aiogram import Bot, Dispatcher, executor
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

setup_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
