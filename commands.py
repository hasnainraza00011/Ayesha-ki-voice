
from aiogram.types import Message

async def help_handler(message: Message):
    await message.answer("/voice - Convert Text to Voice\n/deposit - Deposit Money\n/balance - Check Balance\n/referral - Your Referral\n/proof - Upload Screenshot")

async def learn_handler(message: Message):
    await message.answer("This bot converts your text into voice using Novita.ai API and supports payment features.")
