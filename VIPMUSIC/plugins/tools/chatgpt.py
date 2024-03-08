from VIPMUSIC import app
from VIPMUSIC.core.userbot import Userbot
from VIPMUSIC.utils.database import get_assistant
import requests
import time
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters

@app.on_message(filters.command(["blackai", "bai"], prefixes=["+", ".", "/", "-", "?", "$", "#", "&"]))
async def chat(bot, message):

    try:
        viv = message.chat.id
        userbot = await get_assistant(viv)
        start_time = time.time()
        await userbot.send_chat_action(message.chat.id, ChatAction.TYPING)

        # Check if the message has a reply
        if message.reply_to_message and message.reply_to_message.text:
            user_input = message.reply_to_message.text
        else:
            # If no reply, use the message text directly
            user_input = " ".join(message.command[1:])

        if len(user_input) < 1:
            await userbot.send_message(chat_id=viv, "Example\n\n`/blackai write simple website code using html css, js?`")
        else:
            response = requests.get(f'https://blackai.apinepdev.workers.dev/?question={user_input}')
            x = response.json()["answer"]

            end_time = time.time()
            telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"
            await userbot.send_message(f" {x}", parse_mode=ParseMode.MARKDOWN)

    except Exception as e:
        await userbot.send_message(f"**ᴇʀʀᴏʀ: {e} ")
