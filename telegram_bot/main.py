import telebot
from telebot import types
import random

token = '5936782994:AAE_D66GC203e1xjJYSVgTmCsanvUQNAh1k'

bot = telebot.TeleBot(token)

keyboard = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton('Играть!')
btn2 = types.KeyboardButton('Нет, я пас!')
keyboard.add(btn1, btn2)

@bot.message_handler(commands=['start', 'game'])
def start_message(message):
    bot_message = bot.send_message(message.chat.id, 'Привет пользователь, Начнем нашу игру!', reply_markup=keyboard)
    bot.register_next_step_handler(bot_message, check_answer)

def check_answer(message):
    if message.text == 'Играть!':
        bot.send_message(message.chat.id, 'Ok, тогда лови правила игры:\nНужно угадать число, которое я загадаю в диапозоне от 1 до 10 включительно! У тебя будет 3 попытки! Если не угадаешь, то я тебя повешу! :)')
        number = random.randint(1, 10)
        print(number, '!!!')
        game(message, 3, number)
    elif message.text == 'Нет, я пас!':
        bot.send_message(message.chat.id, 'Net tak Net, Poka')
    else:
        bot_message = bot.send_message(message.chat.id, 'вы ввели неправильный ответ!\n Введите новый: ', reply_markup=keyboard)
        bot.register_next_step_handler(bot_message, check_answer)

def game(message, attempts,number):
    message_bot = bot.send_message(message.chat.id, 'Выбери число: ')
    bot.register_next_step_handler(message_bot, check_number, attempts-1)

def check_number(message, attempts, number):
    if message.text == str(number):
        bot.send_message(message.chat.id, 'Вы победили!')
    elif attempts == 0:
        bot.send_message(message.chat.id, 'Не теряй решимость дитя!')
    else:
        bot.send_message(message.chat.id, 'Нет ты не угадал!')    
        game(message, attempts, number)
        
bot.polling()







