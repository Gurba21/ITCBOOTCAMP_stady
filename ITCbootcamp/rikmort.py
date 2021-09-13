
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
open_weather_token = '4ab6beee1b0d4e1e78004d4797804262'
tg_bot_token = '1999228638:AAHI_M_nyRglqqnpAqqhISiahqggY5CZmKo'

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Рик')
    item2 = types.KeyboardButton("Морти")
    item3 = types.KeyboardButton('Кристиан')
    item4 = types.KeyboardButton('morti')
    item5 = types.KeyboardButton('Бет')
    item6 = types.KeyboardButton('Итан')
    markup.add(item1, item2, item4, item5, item6)
    await message.reply("привет , выбери героя и я дам информацию",reply_markup=markup)
@dp.message_handler(Text(equals="Рик"))
async def with_puree(message: types.Message):
    await message.reply("He's name is : Rick Sanchez\n Status : Alive\n Species : Human\n Gender : Male ")

@dp.message_handler(Text(equals="Морти"))
async def with_puree1(message: types.Message):
    await message.reply("He's name is : Morti Smith\n Status : Alive\n Species : Human\n Gender : Male ")


@dp.message_handler(Text(equals="кристиан"))
async def with_puree2(message: types.Message):
    await message.reply("He's name is : Kristen Stewart\n Status : Alive\n Species : Human\n Gender : Female")

@dp.message_handler(Text(equals="morti"))
async def with_puree3(message: types.Message):
    await message.reply("He's name is : Campaign Manager Morty\n Status : dead\n Species : Human\n Gender : Male")

@dp.message_handler(Text(equals="Бет"))
async def with_puree4(message: types.Message):
    await message.reply("He's name is : Beth Smith\n Status : Alive\n Species : Human\n Gender : Female")

@dp.message_handler(Text(equals="Итан"))
async def with_puree5(message: types.Message):
    await message.reply("He's name is : Ethtan\n Status : Alive\n Species : Human\n Gender : Female")

executor.start_polling(dp)