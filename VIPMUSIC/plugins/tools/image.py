import requests
from requests import get 
from VIPMUSIC import app
from pyrogram import filters
from pyrogram.types import InputMediaPhoto
from VIPMUSIC.core.userbot import Userbot
from VIPMUSIC.utils.database import get_assistant

@app.on_message(filters.command(["image", "img"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def pinterest(_, message):
    chat_id = message.chat.id
    userbot = await get_assistant(chat_id)

    try:
        query = message.text.split(None, 1)[1]
    except IndexError:
        return await message.reply("**ɢɪᴠᴇ ɪᴍᴀɢᴇ ɴᴀᴍᴇ ғᴏʀ sᴇᴀʀᴄʜ 🔍**")

    images = get(f"https://pinterest-api-one.vercel.app/?q={query}").json()

    media_group = []
    count = 0

    msg = await message.reply(f"sᴄʀᴀᴘɪɴɢ ɪᴍᴀɢᴇs ғʀᴏᴍ ᴘɪɴᴛᴇʀᴇᴛs...")

    for url in images["images"][:6]:
        media_group.append(InputMediaPhoto(media=url))
        count += 1
        await msg.edit(f"=> sᴄʀᴀᴘᴇᴅ ɪᴍᴀɢᴇs {count}")

    try:
        await userbot.send_media_group(
            chat_id=chat_id,
            media=media_group,
            reply_to_message_id=message.id
        )
        return await msg.delete()

    except Exception as userbot_error:
        try:
            # Sending using the bot if userbot encounters an issue
            await app.send_media_group(
                chat_id=chat_id,
                media=media_group,
                reply_to_message_id=message.id
            )
            return await msg.delete()
        except Exception as bot_error:
            await msg.delete()
            return await message.reply(f"Both userbot and bot failed to send media group. Userbot Error: {userbot_error}, Bot Error: {bot_error}")