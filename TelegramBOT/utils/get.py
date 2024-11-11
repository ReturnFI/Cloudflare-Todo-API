# utils/get.py

from telebot import TeleBot
import api

def get_todos(bot: TeleBot, message):
    todos = api.get_todos()
    if todos is None:
        bot.send_message(message.chat.id, "Failed to retrieve todos.")
        return
    
    message_text = "\n\n".join([
        f"*ID:* `{todo.get('id', 'N/A')}`\n*Title:* `{todo.get('title', 'No Title')}`\n*Content:* `{todo.get('content', 'No Content')}`"
        for todo in todos
    ])
    
    if not message_text.strip():
        message_text = "No todos available."
    
    bot.send_message(message.chat.id, f"Todos:\n{message_text}", parse_mode='Markdown')
