import requests
from config import BOT_TOKEN

# Replace 'YOUR_BOT_TOKEN' with your actual bot token


# Telegram API endpoint for getting information about the bot
API_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/getMe'

# Make a request to the Telegram API
response = requests.get(API_URL)
data = response.json()

# Extract relevant information
bot_id = data['result']['id']
bot_name = data['result']['first_name']
bot_username = data['result']['username']
bot_mention = f'@{bot_username}'

# Print the obtained information
print(f'Bot ID: {bot_id}')
print(f'Bot Name: {bot_name}')
print(f'Bot Username: {bot_username}')
print(f'Bot Mention: {bot_mention}')