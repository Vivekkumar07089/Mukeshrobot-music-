import requests
from config import BOT_TOKEN
from VIPMUSIC import app
#app is a pyrogram client 

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

# Create a message with bot information
message = f'Bot ID: {BOT_ID}\nBot Name: {BOT_NAME}\nBot Username: {BOT_USERNAME}\nBot Mention: {BOT_MENTION}'

# Use Pyrogram client to send the message (adjust the chat_id accordingly)
app.send_message(chat_id='-1002042572827', text=message)