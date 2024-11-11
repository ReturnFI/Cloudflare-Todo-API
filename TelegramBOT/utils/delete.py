# utils/delete.py

from telebot import TeleBot
import api

def delete_todo_ask_id(bot: TeleBot, message):
    bot.send_message(message.chat.id, "Please send the ID of the todo you want to delete:")
    bot.register_next_step_handler(message, delete_todo, bot)

def delete_todo(message, bot):
    todo_id = message.text
    success = api.delete_todo(todo_id)
    if success:
        bot.send_message(message.chat.id, f"Todo {todo_id} deleted successfully.")
    else:
        bot.send_message(message.chat.id, f"Failed to delete todo {todo_id}.")
