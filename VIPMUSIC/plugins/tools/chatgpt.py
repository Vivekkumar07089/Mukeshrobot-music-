from VIPMUSIC import app
from pyrogram import filters
import requests
from pyrogram.enums import ChatAction
from VIPMUSIC.core.userbot import Userbot
from VIPMUSIC.utils.database import get_assistant

@app.on_message(filters.command(["chatgpt", "ai", "ask"], prefixes=["+", ".", "/", "-", "?", "$", "#", "&"]))
async def chatgpt_chat(bot, message):
    chat_id = message.chat.id
    userbot = await get_assistant(chat_id)

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

            try:
                await userbot.send_message(chat_id, f"Question: {user_input}\n\nANS:- {result}", quote=True)
            except Exception as e:
                # Log the exception (optional)
                print(f"Userbot failed to send message: {e}")
                
                # Use the main bot ('app') as a fallback
                await app.send_message(chat_id, f"Question: {user_input}\n\nANS:- {result}")
        else:
            pass
    except requests.exceptions.RequestException as e:
        # Handle request exceptions (optional)
        print(f"Request failed: {e}")