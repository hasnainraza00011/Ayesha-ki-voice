
from aiogram import Dispatcher
from handlers.voice import voice_handler
from handlers.deposit import deposit_handler
from handlers.balance import balance_handler
from handlers.referral import referral_handler
from handlers.screenshot import screenshot_handler
from handlers.commands import help_handler, learn_handler

def setup_handlers(dp: Dispatcher):
    dp.register_message_handler(voice_handler, commands=["voice"])
    dp.register_message_handler(deposit_handler, commands=["deposit"])
    dp.register_message_handler(balance_handler, commands=["balance"])
    dp.register_message_handler(referral_handler, commands=["referral"])
    dp.register_message_handler(screenshot_handler, commands=["proof"])
    dp.register_message_handler(help_handler, commands=["help"])
    dp.register_message_handler(learn_handler, commands=["learn"])
