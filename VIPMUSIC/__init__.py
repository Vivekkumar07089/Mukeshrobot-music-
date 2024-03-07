from VIPMUSIC.core.bot import VIP
from VIPMUSIC.core.dir import dirr
from VIPMUSIC.core.git import git
from VIPMUSIC.core.userbot import Userbot
from VIPMUSIC.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = VIP()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()


getme = app.get_me()
BOT_ID = getme.id
BOT_NAME = getme.first_name
BOT_USERNAME = getme.username
BOT_MENTION = getme.mention

"""
async def get_bot_info():
    getme = await app.get_me()
    BOT_ID = getme.id
    BOT_NAME = getme.first_name
    BOT_USERNAME = getme.username
    BOT_MENTION = getme.mention
    
    # Returning the values
    return BOT_ID, BOT_NAME, BOT_USERNAME, BOT_MENTION

# Call the function to get the bot info
BOT_ID, BOT_NAME, BOT_USERNAME, BOT_MENTION = await get_bot_info()
"""