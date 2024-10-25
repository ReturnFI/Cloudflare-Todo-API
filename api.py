# api.py

import requests
import os
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_URL = os.getenv("API_URL")
UUID_HEADER = json.loads(os.getenv("UUID_HEADER"))

def get_todos():
    response = requests.get(API_URL, headers=UUID_HEADER)
    if response.status_code == 200:
        return response.json()
    return None

def add_todo(title, content):
    new_todo = {"title": title, "content": content}
    response = requests.post(API_URL, json=new_todo, headers=UUID_HEADER)
    if response.status_code == 201:
        return response.json()
    return None

def update_todo(todo_id, title, content):
    updated_todo = {"title": title, "content": content}
    response = requests.put(f"{API_URL}?id={todo_id}", json=updated_todo, headers=UUID_HEADER)
    return response.status_code == 200

def delete_todo(todo_id):
    response = requests.delete(f"{API_URL}?id={todo_id}", headers=UUID_HEADER)
    return response.status_code == 200
