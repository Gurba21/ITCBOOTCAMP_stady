import requests
import datetime
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from pprint import pprint as pp

open_weather_token = 'f23a3922d2bc1ae32533c394122e68a1'
tg_bot_token = '1975257685:AAHveFvMyv47m5MZCcqd4NRv6jN3vd0B-cc'


bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Здарвствуйте,введите город")

@dp.message_handler()
async def get_weather(message: types.message):
    code_to_smile = {
        'Clear' : 'Ясно \U0001F601',
        'Clouds' : 'Облачно \U0001F972',
        'Sunrise' : 'Рассвет \U0001F304',
        'Sunset' : 'Закат \U0001F307',
        'Rain' : 'Дождливо \U0001F327',
        'Snow' : 'Снег \U0001F328',
        'Mist' : 'Туманно \U0001F32B'
}


    try:
        r = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric')
        data = r.json()

        city = data['name']
        weather_description = data['weather'][0]['main']
        temp = data['main']['temp']
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Я не предусмотрел такую иконку погоды потому что все сейсач сдохнут от скуки посмотри в окно"

        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        weather = data['weather'][0]['main']
        wind = data['wind']['speed']


        await message.reply(f"Город {city}\n Влажность {humidity}\n Давляна {pressure}\n Темпратура {temp}\n Романтика {sunrise}\n Восход {sunset}\n Облачность {weather}\n Скорость ветра {wind}")

    except:
        await message.reply("Эй делдирееек напиши название города правильно ")


executor.start_polling(dp)