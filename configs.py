from os import getenv as genv
from pyrogram import Client

API_ID = genv("API_ID", "22977776")

API_HASH = genv("API_HASH", "2ac7223d720bdeec757cbc88ced57224")

BOT_TOKEN = genv("BOT_TOKEN", "7551999112:AAHfWb5P1THjOokzGbMbdkIR-MxztgWVWTI")

SUPPORT_GROUP = genv("SUPPORT_GROUP", "TGHelpingGroup")

UPDATES_CHANNEL = genv("UPDATES_CHANNEL", "TamizhFiles")

GROUP_ID = int(genv("GROUP_ID", "-1002341945360"))

DATABASE_URL = genv(
    "DATABASE_URL",
    "mongodb+srv://jeevanantham8157:1055221@filestorebot.rahsk.mongodb.net/?retryWrites=true&w=majority&appName=Filestorebot",
)

USER_SESSION_STRING = genv(
    "USER_SESSION_STRING",
    "BQFenPAAIj8e87KgL7udCHfbbxaz71kTBdVeYtMBpJ1fuZt_9OSljhfRrGmm6oeIWHR0l7tnKaP4HgMZvk1GcnMnAVhhiOu3ajAc8I7bOM5TnsHPzIZhdT0csFKURrUGy5twYCJe81oWKCHEwzk2Y-NUoSpPCKM5OXTuErgc1qDadOZZEn0_jMsCF9RqZoXOvcs3ZfCtjc3apZZb53MLWyp3CxVbnTj-5va-pPfxqKrwVZqI38LpM5hby7UAkT7EaKT2cpDDB8f285C33SB_vQFxBtKLh70yhVU9hooQf-ZK7yGiXQMWUcT4R1_X5xAbI4yOCm45UGZA048EiDfGmbNJGeGS1QAAAAGTFHWXAA",
)

SERVER_URL = genv("SERVER_URL", "https://heartxscrapper.koyeb.app/")


RSS_CHAT = int(
    genv("RSS_CHAT", "-1002426963681")
)  # add the channel id where the torrent files need to be sent

BASE_URL = genv(
    "BASE_URL", "https://www.1tamilmv.ac"
).lower()  # update the main domain if changed



#change the theme as you required



START_TXT = """<b>Hello {}, I am a Scrapper Bot!.
๏ I can scrap links from 1tamilmv and update it in Bot..
๏ Click on the help menu button below to get information about my commands.
๏ Powered By @HeartXbotz</b>"""


HELP_TXT = """Send any Movie Name and I will provide torrent links.

Available Commands

-> /get - To Get Torrent Link of that Movie
-> /list - To get last 10 Movie/Series details

Updates - ⍟ @HeartXBotz"""

ABOUT_TXT = """<b>╔════❰ Tʙ Sʜᴏʀᴛɴᴇʀ Bᴏᴛ ❱═══❍
║ ┏━━━━━━━━━❥
║ ┣ Mʏ ɴᴀᴍᴇ -> {}
║ ┣ Uᴘᴅᴀᴛᴇꜱ -> <a href="tg://HeartXBotz">••Bᴏᴛs••</a>
║ ┣ 𝖲ᴜᴘᴘᴏʀᴛ -> <a href="tg://TGHelpingGroup"> Bᴏᴛs Sᴜᴩᴩᴏʀᴛ</a>
║ ┣ ๏ Cʜᴇᴄᴋ ʜᴇʟᴘ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ.
║ ┗━━━━━━━━━❥
╚═════❰ @ ❱═════❍</b>"""


WEEK_RELEASES_PATH = genv("RELEASES_PATH", "/index.php?/forums/topic/")  # dont change this
