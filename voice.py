
from aiogram.types import Message

async def voice_handler(message: Message):
    await message.answer("Send your text to convert into voice...")
