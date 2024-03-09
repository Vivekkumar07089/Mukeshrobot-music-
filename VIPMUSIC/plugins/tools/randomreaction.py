import random
from pyrogram.types import Message
from pyrogram import Client, filters
from VIPMUSIC import app
from VIPMUSIC.core.userbot import Userbot
from VIPMUSIC.utils.database import get_assistant

reaction_list = ["🔥", "😊", "👍", "💬", "🎉"]  # Add your desired reactions

@app.on_message(filters.private | filters.group)
async def send_random_reaction(client, message):
    if "/" in message.text:
        random_reaction = random.choice(reaction_list)
        await app.send_reaction(message.chat.id, message.message_id, random_reaction)

@app.on_message(filters.private | filters.group)
async def send_v_random_reaction(client, message):
    if "/" in message.text:
        userbot = await get_assistant(message.chat.id)
        random_reaction = random.choice(reaction_list)
        await userbot.send_reaction(message.chat.id, message.message_id, random_reaction)