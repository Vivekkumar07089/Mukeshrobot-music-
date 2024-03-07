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

from botinfo import BOT_NAME, BOT_USERNAME, BOT_ID, BOT_MENTION

BOT_MENTION = BOT_MENTION
BOT_ID = BOT_ID
BOT_NAME = BOT_NAME
BOT_USERNAME = BOT_USERNAME
