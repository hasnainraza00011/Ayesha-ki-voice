from aiogram import types
from config import ADMIN_ID

async def upload_payment_ss_handler(message: types.Message):
    if not message.photo:
        return await message.reply("📸 Please upload payment screenshot.")

    await message.reply("✅ Payment screenshot received. We'll verify it soon.")
    await message.bot.send_photo(
        chat_id=ADMIN_ID,
        photo=message.photo[-1].file_id,
        caption=f"💰 Payment Screenshot from @{message.from_user.username}"
    )