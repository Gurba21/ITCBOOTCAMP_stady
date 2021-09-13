# import telebot
# from telebot import types
#
# API = '1969798606:AAEzIrKeR5gCxQJ6B6m3PtfT117U-M6YS58'
#
# bot = telebot.TeleBot(API)
# @bot.message_handler(commands=['start'])
# def welocme(message):
#     gif = open('AnimatedSticker.tgs','rb')
#     bot.send_sticker(message.chat.id,gif)
#
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     button1 = types.KeyboardButton("Что будешь покупать?")
#     button2 = types.KeyboardButton("давай до свидания")
#     markup.add(button1,button2)
#
#     bot.send_message(
#         message.chat.id,
#     f"Как ты",
#     reply_markup=markup
#     )
#
# @bot.message_handler(commands=['info'])
# def info(message):
#     bot.reply_to(message,"i am testBot")
#
#
#
# @bot.message_handler(content_types=['text'])
# def echo(message):
#     markup = types.InlineKeyboardMarkup(row_width=2)
#     button1 = types.InlineKeyboardButton("sale",callback_data='sale')
#     button2 = types.InlineKeyboardButton("buy",callback_data='buy')
#     markup.add(button1,button2)
#     bot.send_message(message.chat.id,message.text,reply_markup=markup)
#
# @bot.callback_query_handler(func=lambda call:True)
# def callback_inline(call):
#     if call.data == "sale":
#         bot.send_message(call.message.chat.id,"sold")
#     elif call.data == 'buy':
#         bot.send_message(call.message.chat.id,"buyed")
#
#     bot.edit_message_text(
#         chat_id=call.messange.chat.id,
#         message_id=call.messange.chat_id,
#         text = "do you want?",
#         reply_markup=None
#     )
#
# bot.polling()


import telebot
from telebot import types
import random

API = '1990020092:AAEV0ieZbl96oJ1dpADw6LROMBn3vW3HQfM'

bot = telebot.TeleBot(API)

@bot.message_handler(commands=['start'])
def welcome(message):
    gif = open('day10.py', 'rb')
    bot.send_sticker(message.chat.id, gif)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Рандом")
    button2 = types.KeyboardButton("Продолжение")
    markup.add(button1, button2)

    bot.send_message(
        message.chat.id,
        f"Калайсын тайсын",
        reply_markup=markup
    )

@bot.message_handler(commands=['info'])
def info(message):
    bot.reply_to(message, "Это тестовый телеграм бот")


@bot.message_handler(content_types=['text'])
def echo(message):
    if message.text == "Рандом":
        bot.send_message(message.chat.id, str(random.randint(1, 10000000)))
    elif message.text == "Продолжение":
        markup = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Продать",callback_data='Продать')
        button2 = types.InlineKeyboardButton("Купить", callback_data='Купить')
        markup.add(button1, button2)
        bot.send_message(message.chat.id, message.text, reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "qweqwewqe")
@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    if call.data == 'Продать':
        bot.send_message(call.message.chat.id, 'Проданно')
    elif call.data == 'Купить':
        bot.send_message(call.message.chat.id, 'Купленно')

    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text = "Что хочешь?",
        reply_markup=None
    )


bot.polling()