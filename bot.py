import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from handlers import different_types

logging.basicConfig(level=logging.INFO)
bot = Bot(token="7117099158:AAHInAsNiinlXbFV5BnY6CILmeNZeEXh3jc")
dp = Dispatcher()
dp.include_router(different_types.router)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет, пришли мне фотографию, а я тебе скажу, кто ней."
                         "\nНо учти то, что я могу работать только с фотографиями в формате jpeg и то,"
                         " что я могу не узнать всё на картинке")

@dp.message(Command("help"))
async def help_me(message: types.Message):
    await message.answer("/start -- Увидеть приветственное сообщение"
                         "\n/help -- Увидеть это сообщение")
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
