
from aiogram.types import Message

async def balance_handler(message: Message):
    await message.answer("Your balance is 0 PKR (demo).")
