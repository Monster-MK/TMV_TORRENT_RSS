from os import getenv as genv
from pyrogram import Client

API_ID = genv("API_ID", "22977776")

API_HASH = genv("API_HASH", "2ac7223d720bdeec757cbc88ced57224")

BOT_TOKEN = genv("BOT_TOKEN", "7692272341:AAEcqZkFIx6Y6iljv96xt3SXSNwGY4_V8O4")

SUPPORT_GROUP = genv("SUPPORT_GROUP", "TGHelpingGroup")

UPDATES_CHANNEL = genv("UPDATES_CHANNEL", "PlayTamilX")

GROUP_ID = int(genv("GROUP_ID", "-1002341945360"))

DATABASE_URL = genv(
    "DATABASE_URL",
    "mongodb+srv://jeevanantham8157:1055221@leechbot.gpkuo.mongodb.net/?retryWrites=true&w=majority&appName=Leechbot",
)

USER_SESSION_STRING = genv(
    "USER_SESSION_STRING",
    "BQFenPAAex8_E-w7zEYSx1xuL5bi7Gv8VU6UIGMzQqoYaHsfkLQmnliZaCCXWyEvmDMwuQvnRnSEhhbI7qfbSSRWXb0qoUFfelbRpnZg7pc3n1YD06OwyktUpV6ZJYNHpLpvHQB2hKlXSD8SW3fu4iEZ9y_9Hbwjv12_6ZCAqUstedBTiB1MRMnSD_2QGt1hvWpYFymzC0yVsyJyv27t67p_EJ5g8veL2OwGUduc7XdZffDqhGF1ZSr8ph9kjZA2RLOflYPiE36VX9JvpahRUyfS2uyVHaNufs-2pzxpub86VA9d_0LHLC4FiK3WlnGCr5O62NDmgb082hjP2BeUayX-S37ftgAAAAGTFHWXAA",
)

SERVER_URL = genv("SERVER_URL", "https://scraptestmadx-ed1ff622ea8c.herokuapp.com/")


RSS_CHAT = int(
    genv("RSS_CHAT", "-1002335041395")
)  # add the channel id where the torrent files need to be sent

BASE_URL = genv(
    "BASE_URL", "https://www.1tamilmv.fit"
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
