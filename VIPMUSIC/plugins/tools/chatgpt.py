from VIPMUSIC import app
from pyrogram import filters
import requests
import time
from pyrogram.enums import ChatAction, ParseMode
from VIPMUSIC.core.userbot import Userbot
from VIPMUSIC.utils.database import get_assistant


@app.on_message(filters.command(["chatgpt", "ai", "ask"], prefixes=["+", ".", "/", "-", "?", "$", "#", "&"]))
async def chatgpt_chat(bot, message):
    if len(message.command) < 2 and not message.reply_to_message:
        await message.reply_text("Example:\n\n`/ai write simple website code using html css, js?`")
        return

    if message.reply_to_message and message.reply_to_message.text:
        user_input = message.reply_to_message.text
    else:
        user_input = ' '.join(message.command[1:])

    try:
        response = requests.get(f'https://mukesh-api.vercel.app/chatgpt?query={user_input}')
        if response.status_code == 200:
            await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
            result = response.json()["results"]
            await message.reply_text(f"{result}", quote=True)
        else:
            pass
    except requests.exceptions.RequestException as e:
        pass


@app.on_message(filters.command(["blackai", "bai"], prefixes=["+", ".", "/", "-", "?", "$", "#", "&"]))
async def chat(bot, message):

    try:
        start_time = time.time()
        await app.send_chat_action(message.chat.id, ChatAction.TYPING)

        # Check if the message has a reply
        if message.reply_to_message and message.reply_to_message.text:
            user_input = message.reply_to_message.text
        else:
            # If no reply, use the message text directly
            user_input = " ".join(message.command[1:])

        if len(user_input) < 1:
            await message.reply_text("**EXAMPLE**\n\n`/blackai who is lord Ram tell in hindi`")
        else:
            response = requests.get(f'https://blackai.apinepdev.workers.dev/?question={user_input}')
            x = response.json()["answer"]

            end_time = time.time()
            telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"
            await message.reply_text(f" {x}", parse_mode=ParseMode.MARKDOWN)

    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ: {e} ")
__mod_name__ = "Cʜᴀᴛɢᴘᴛ"
__help__ = "/ai - ᴀsᴋ ʏᴏᴜʀ ǫᴜᴇʀʏ ᴛᴏ ᴄʜᴀᴛɢᴘᴛ\n/blackai - ᴀsᴋ ʏᴏᴜʀ ǫᴜᴇsᴛɪᴏɴ ᴡɪᴛʜ ʙʟᴀᴄᴋᴀɪ\n/gemini - ᴀsᴋ ʏᴏᴜʀ ǫᴜᴇsᴛɪᴏɴ ᴡɪᴛʜ ɢᴏᴏɢʟᴇ's ɢᴇᴍɪɴɪ"