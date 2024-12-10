from os import getenv as genv
from pyrogram import Client

API_ID = genv("API_ID", "22977776")

API_HASH = genv("API_HASH", "2ac7223d720bdeec757cbc88ced57224")

BOT_TOKEN = genv("BOT_TOKEN", "7551999112:AAHfWb5P1THjOokzGbMbdkIR-MxztgWVWTI")

SUPPORT_GROUP = genv("SUPPORT_GROUP", "TGHelpingGroup")

UPDATES_CHANNEL = genv("UPDATES_CHANNEL", "TamizhFiles")

GROUP_ID = int(genv("GROUP_ID", "-1002325685641"))

DATABASE_URL = genv(
    "DATABASE_URL",
    "mongodb+srv://jeevanantham8157:1055221@leechbot.gpkuo.mongodb.net/?retryWrites=true&w=majority&appName=Leechbot",
)

USER_SESSION_STRING = genv(
    "USER_SESSION_STRING",
    "BQFenPAATUkq6dj37A_neoS6WU1_TbdRZzcIrAdQeNEW7njkXqhw9u7fJN8tN1VItUcE_ps35NzaY6gwxmY6l7MLD76rooMUcdd7uiBAa4f-GOBU_i3FcVZi6eMmMP-sq45T6W7uy-0Gc2LjAJA2oaHFfiIqJABEOwggWC0y6-hLZgK4fMkWHtTBygOioFVFZ23JNEI5nT7iNflhJ3vxcVtAD5YZ_mBgkXIPS99iMioD4Id4K5q4_kNtDOUzkKr9GyCikjqxBvEO2I4oOWKwvSnD0cpipQJpnnxni7kuhN_T1TNgoxapvtXfYEyGjhBuaGEl2NBD_PYtBCH1gQbO_U6ZU8gMxwAAAAGTFHWXAA",
)

SERVER_URL = genv("SERVER_URL", "https://scraptestmadx-ed1ff622ea8c.herokuapp.com/")


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
๏ Powered By @TamilXLeech</b>"""


HELP_TXT = """Send any Movie Name and I will provide torrent links.

Available Commands

-> /get - To Get Torrent Link of that Movie
-> /list - To get last 10 Movie/Series details

Updates - ⍟ @TamilxLeech"""

ABOUT_TXT = """<b>╔════❰ Tʙ Sʜᴏʀᴛɴᴇʀ Bᴏᴛ ❱═══❍
║ ┏━━━━━━━━━❥
║ ┣ Mʏ ɴᴀᴍᴇ -> {}
║ ┣ Uᴘᴅᴀᴛᴇꜱ -> <a href="tg://TamilXLeech">••Bᴏᴛs••</a>
║ ┣ 𝖲ᴜᴘᴘᴏʀᴛ -> <a href="tg://TGHelpingGroup"> Bᴏᴛs Sᴜᴩᴩᴏʀᴛ</a>
║ ┣ ๏ Cʜᴇᴄᴋ ʜᴇʟᴘ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ.
║ ┗━━━━━━━━━❥
╚═════❰ @ ❱═════❍</b>"""


WEEK_RELEASES_PATH = genv("RELEASES_PATH", "/index.php?/forums/topic/")  # dont change this
