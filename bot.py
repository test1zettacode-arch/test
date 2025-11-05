from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, KeyboardButton,ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.default import DefaultBotProperties

import logging


logging.basicConfig(level=logging.INFO)

bot = Bot('8441274720:AAG-RWg-JNaFC6hGC1aCjuFrdbqAn9tGm8Y', default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='app', web_app=WebAppInfo(url=f'https://test1zettacode-arch.github.io/test/'))],
    ])


@dp.message(CommandStart())
async def func(message: Message):
    await message.answer('Добро пожаловать',
                            reply_markup=kb)


async def start():
    await dp.start_polling(bot)
