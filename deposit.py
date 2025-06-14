
from aiogram.types import Message
from config import USDT_ADDRESS, EASYPAISA_NAME, EASYPAISA_NUMBER

async def deposit_handler(message: Message):
    await message.answer(f"Deposit Options:\nUSDT: {USDT_ADDRESS}\nEasypaisa: {EASYPAISA_NAME} - {EASYPAISA_NUMBER}")
