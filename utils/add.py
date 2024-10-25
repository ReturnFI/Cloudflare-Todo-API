# utils/add.py

from telebot import TeleBot
import api

user_data = {}

def add_todo_ask(bot: TeleBot, message):
    bot.send_message(message.chat.id, "Please send the title for the todo:")
    bot.register_next_step_handler(message, add_todo_ask_content, bot)

def add_todo_ask_content(message, bot):
    user_data[message.chat.id] = {"title": message.text}
    bot.send_message(message.chat.id, "Please send the content for the todo:")
    bot.register_next_step_handler(message, add_todo, bot)

def add_todo(message, bot):
    title = user_data[message.chat.id]['title']
    content = message.text
    todo = api.add_todo(title, content)
    if todo:
        bot.send_message(message.chat.id, f"Todo added successfully: `{todo['id']}`", parse_mode='Markdown')
    else:
        bot.send_message(message.chat.id, "Failed to add todo.")
