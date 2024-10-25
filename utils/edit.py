# utils/edit.py

from telebot import TeleBot
import api

# Temporary data storage
user_data = {}

def edit_todo_ask_id(bot: TeleBot, message):
    bot.send_message(message.chat.id, "Please send the ID of the todo you want to edit:")
    bot.register_next_step_handler(message, edit_todo_ask_title, bot)

def edit_todo_ask_title(message, bot):
    user_data[message.chat.id] = {"todo_id": message.text}
    bot.send_message(message.chat.id, "Please send the new title for the todo:")
    bot.register_next_step_handler(message, edit_todo_ask_content, bot)

def edit_todo_ask_content(message, bot):
    user_data[message.chat.id]['new_title'] = message.text
    bot.send_message(message.chat.id, "Please send the new content for the todo:")
    bot.register_next_step_handler(message, edit_todo, bot)

def edit_todo(message, bot):
    todo_id = user_data[message.chat.id]['todo_id']
    new_title = user_data[message.chat.id]['new_title']
    new_content = message.text
    success = api.update_todo(todo_id, new_title, new_content)
    if success:
        bot.send_message(message.chat.id, f"Todo {todo_id} updated successfully.")
    else:
        bot.send_message(message.chat.id, f"Failed to update todo {todo_id}.")
