import asyncio
import random
from aiogram import F, Bot, Dispatcher, types
from aiogram.filters import CommandStart

bot = Bot('7226441546:AAGqsYgK0XoToSRoLs1PVSZuWCT5t26P4E4')
bot.my_admins_list = []

dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Привет, вы снова бесите друг-друга? Ну что ж, я помогу вам решить, кто из вас!")

@dp.message(F.text)
async def message(message: types.Message):
   
    if(random.randint(1, 2) == 1):   
        file_path = "image/Edo.jpg"
        await message.reply_photo(photo=types.FSInputFile(path=file_path), caption="Чип")
    else:
        file_path = "image/Dasha.jpg"
        await message.reply_photo(photo=types.FSInputFile(path=file_path),caption="Гайка") 


async def main():
   await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

asyncio.run(main())