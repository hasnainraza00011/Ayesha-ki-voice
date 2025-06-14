from aiogram import types

async def help_handler(message: types.Message):
    await message.answer(
        "🆘 *Help Menu*\n\n"
        "/start – Bot shuru karne ke liye\n"
        "/voice – Voice convert karne ke liye\n"
        "/deposit – Paise jama karne ke options\n"
        "/balance – Aapka balance dekhne ke liye\n"
        "/referral – Referral link aur rewards\n"
        "/upload_ss – Upload payment screenshot proof\n"
        "/plans – Plans dekhne ke liye\n"
        "/learn – Bot ka istemal seekhne ke liye",
        parse_mode=types.ParseMode.MARKDOWN
    )