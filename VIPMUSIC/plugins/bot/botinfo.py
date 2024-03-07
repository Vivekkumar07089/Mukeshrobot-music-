import requests
from config import BOT_TOKEN
from pyrogram import filters
from VIPMUSIC import app

# Define a command handler for /botinfo
@app.on_message(filters.command("botinfo"))
async def bot_info_command(client, message):
    await send_bot_info(message.chat.id)

async def send_bot_info(chat_id):
    # Telegram API endpoint for getting information about the bot
    API_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/getMe'

    # Make a request to the Telegram API
    response = requests.get(API_URL)
    data = response.json()

    # Extract relevant information
    BOT_ID = data['result']['id']
    BOT_NAME = data['result']['first_name']
    BOT_USERNAME = data['result']['username']
    BOT_MENTION = f'[{BOT_NAME}](https://t.me/{BOT_USERNAME})'  # Fix the link format

    # Create a message with bot information
    message = f'Bot ID: {BOT_ID}\nBot Name: {BOT_NAME}\nBot Username: {BOT_USERNAME}\nBot Mention: {BOT_MENTION}'

    # Use Pyrogram client to send the message
    await app.send_message(chat_id=chat_id, text=message)

