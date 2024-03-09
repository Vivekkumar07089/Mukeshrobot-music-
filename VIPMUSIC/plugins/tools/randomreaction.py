import random
from VIPMUSIC import app
from VIPMUSIC.core.userbot import Userbot
from VIPMUSIC.utils.database import get_assistant

reaction_list = ["🔥", "😊", "👍", "💬", "🎉"]  # Add your desired reactions



@app.on_message(filters.private | filters.group)
async def send_random_reaction(client, message):
    chat_id = message.chat.id
    message_id = message.message_id
    
    if "/" in message.text:
        random_reaction = random.choice(reaction_list)
        await app.send_reaction(chat_id, message_id, random_reaction)


@app.on_message(filters.private | filters.group)
async def send_v_random_reaction(client, message):
    chat_id = message.chat.id
    message_id = message.message_id
    userbot = await get_assistant(chat_id)
    
    if "/" in message.text:
        random_reaction = random.choice(reaction_list)
        await userbot.send_reaction(chat_id, message_id, random_reaction)

