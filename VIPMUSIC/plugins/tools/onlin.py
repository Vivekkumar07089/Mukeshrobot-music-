from pyrogram import Client, filters
from pyrogram.types import User
from VIPMUSIC import app


# Variable to store online users
online_users = []

# Command handler for /viv
@app.on_message(filters.command("viv"))
def viv_command_handler(client, message):
    global online_users
    # Get all members in the chat
    chat_id = message.chat.id
    chat_members = client.get_chat_members(chat_id)

    # Filter and append online users
    online_users = [
        user.user_id for user in chat_members if user.status == User.STATUS_ONLINE
    ]

    # Send the list of online users as a mention list
    mention_list = " ".join([f"@{user}" for user in online_users])
    message.reply_text(f"Online users: {mention_list}")
