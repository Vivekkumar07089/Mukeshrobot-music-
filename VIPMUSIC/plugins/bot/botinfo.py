import requests
from config import BOT_TOKEN

# Telegram API endpoint for getting information about the bot
API_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/getMe'

# Make a request to the Telegram API
response = requests.get(API_URL)
data = response.json()

# Extract relevant information
BOT_ID = data['result']['id']
BOT_NAME = data['result']['first_name']
BOT_USERNAME = data['result']['username']
BOT_MENTION = f'[{BOT_NAME}](Https://t.me/{BOT_USERNAME})'

# Print the obtained information
print(f'Bot ID: {bot_id}')
print(f'Bot Name: {bot_name}')
print(f'Bot Username: {bot_username}')
print(f'Bot Mention: {bot_mention}')