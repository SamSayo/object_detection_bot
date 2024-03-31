import time
import importlib
from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message
import main

bot = Bot(token="7117099158:AAHInAsNiinlXbFV5BnY6CILmeNZeEXh3jc")
dp = Dispatcher()
router = Router()

@router.message(F.text)
async def message_with_text(message: Message):
    await message.answer("Я не понимаю")

@router.message(F.sticker)
async def message_with_sticker(message: Message):
    await message.answer("Я не понимаю")

@router.message(F.animation)
async def message_with_gif(message: Message):
    await message.answer("Я не понимаю")

@router.message(F.photo)
async def message_with_pics(message: Message):
    importlib.reload(main)
    await message.answer("Погоди, устанавливаю кто тут есть")
    await message.bot.download(file=message.photo[-1].file_id, destination='man.jpg')
    importlib.reload(main)
    print(main.labels)
    await message.answer(text=f"Я вижу {main.labels}")
