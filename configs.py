from os import getenv as genv
from pyrogram import Client

API_ID = genv("API_ID", "22977776")

API_HASH = genv("API_HASH", "2ac7223d720bdeec757cbc88ced57224")

BOT_TOKEN = genv("BOT_TOKEN", "7765333178:AAGfUSmTatPWNxVjdlm5zkjAKySYUn0w3SA")

SUPPORT_GROUP = genv("SUPPORT_GROUP", "TGHelpingGroup")

UPDATES_CHANNEL = genv("UPDATES_CHANNEL", "TamizhFiles")

GROUP_ID = int(genv("GROUP_ID", "-1002539559622"))

DATABASE_URL = genv(
    "DATABASE_URL",
    "mongodb+srv://jeevanantham8157:1055221@filestorebot.rahsk.mongodb.net/?retryWrites=true&w=majority&appName=Filestorebot",
)

USER_SESSION_STRING = genv(
    "USER_SESSION_STRING",
    "BQFenPAAcsILCXJBkxTJ67gXJseKf-SKbRVgP6L2nJ5Yj8yPZSOp0SEKAeUPH3hIXrFPbuT85RHy8vNUwopv0yuGQBfjWGt2tmStQXPK0uKWMUuK0Wre5nerE0wNjl_j0DIaKhh2hwucH_B1ciayGsk_jmXwslnz8foCsGUZdFMqlQmXg4WkT9SL2kHxqgf15Pe4OXVV1P8bfz2_9bmYDQUsCtSKQtz3CxcymAG5-VXCgLrnSCkAYeJykNyfZfA2EACMnR2xTTg0IW2RStQCcFrQZvOL2UQfxEuBYSJhYcQJLxye9v8rxaBwc-dEpmzhtDBARkgtHbdpEw4EaVSAdMV3ezQksgAAAAHBsGPqAA",
)

SERVER_URL = genv("SERVER_URL", "https://heartxscrapper.koyeb.app/")


RSS_CHAT = int(
    genv("RSS_CHAT", "-1002639178211")
)  # add the channel id where the torrent files need to be sent

"""BASE_URL = genv(
    "BASE_URL", "https://www.1tamilmv.com"
).lower() """ # update the main domain if changed

BASE_URL = genv("BASE_URL", "https://www.1tamilmv.ms").lower() # update the main domain if changed

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

ABOUT_TXT = """<b>╔════❰ HeartXBotz ❱═══❍
║ ┏━━━━━━━━━❥
║ ┣ Mʏ ɴᴀᴍᴇ -> {}
║ ┣ Uᴘᴅᴀᴛᴇꜱ -> <a href="tg://HeartXBotz">••Bᴏᴛs••</a>
║ ┣ 𝖲ᴜᴘᴘᴏʀᴛ -> <a href="tg://TGHelpingGroup"> Bᴏᴛs Sᴜᴩᴩᴏʀᴛ</a>
║ ┣ ๏ Cʜᴇᴄᴋ ʜᴇʟᴘ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ.
║ ┗━━━━━━━━━❥
╚═════❰ @HeartThieft ❱═════❍</b>"""


WEEK_RELEASES_PATH = genv("RELEASES_PATH", "/index.php?/forums/topic/")  # dont change this
