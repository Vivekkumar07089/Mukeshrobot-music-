import random
from pyrogram import Client, filters
from VIPMUSIC import app
from VIPMUSIC.core.userbot import Userbot
from VIPMUSIC.utils.database import get_assistant

reaction_list =  ["👍", "👎", "❤", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", "🤬", "😢", "🎉", "🤩", "🤮", "💩", "🙏", "👌", "🕊", "🤡", "🥱", "🥴", "😍", "🐳", "❤‍🔥", "🌚", "🌭", "💯", "🤣", "⚡", "🍌", "🏆", "💔", "🤨", "😐", "🍓", "🍾", "💋", "🖕", "😈", "😴", "😭", "🤓", "👻", "👨‍💻", "👀", "🎃", "🙈", "😇", "😨", "🤝", "✍", "🤗", "🫡", "🎅", "🎄", "☃", "💅", "🤪", "🗿", "🆒", "💘", "🙉", "🦄", "😘", "💊", "🙊", "😎", "👾", "🤷‍♂", "🤷", "🤷‍♀", "😡"]  # Add your desired reactions


@app.on_message(filters.private | filters.group)
async def send_v_random_reaction(_, message):
    if "/" in message.text:
        userbot = await get_assistant(message.chat.id)
        chat_id = message.chat.id

        random_reaction = random.choice(reaction_list)
        await userbot.send_reaction(chat_id, message.id, random_reaction)
