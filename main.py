# main.py

import telebot
import os
from dotenv import load_dotenv
from utils import get_todos, add_todo_ask, edit_todo_ask_id, delete_todo_ask_id

load_dotenv()
API_TOKEN = os.getenv("TELEGAMAPI")
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Get Todos', 'Add Todo')
    markup.row('Edit Todo', 'Delete Todo')
    bot.send_message(message.chat.id, "Welcome! Choose an option:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Get Todos")
def handle_get_todos(message):
    get_todos(bot, message)

@bot.message_handler(func=lambda message: message.text == "Add Todo")
def handle_add_todo(message):
    add_todo_ask(bot, message)

@bot.message_handler(func=lambda message: message.text == "Edit Todo")
def handle_edit_todo(message):
    edit_todo_ask_id(bot, message)

@bot.message_handler(func=lambda message: message.text == "Delete Todo")
def handle_delete_todo(message):
    delete_todo_ask_id(bot, message)

bot.polling()
