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
    "mongodb+srv://jeevanantham8157:1055221@filestorebot.rahsk.mongodb.net/?retryWrites=true&w=majority&appName=Filestorebot",
)

USER_SESSION_STRING = genv(
    "USER_SESSION_STRING",
    "BQFenPAAWqT4IqgTIR0OsPFdWjI6LVao_XaMibQMlX2zEP2d9tBVkwwrf9fGWOQ2dREbzuAKsZA7v1h4niNhBq3KCPn_5l59YApWXN6bZFSzXuopgK5no2rVilAR_KUheq4gyu0WqGqaAkbGl1hrk1BVzUqtgXeMLGxyuGP7fY-5gePl87foPDfVapGUXp64D4bIMWOmyTTiuWzq3is6gRpA6HohNb_9J4t_fK_Q1i721hBQ8W052-vg4lICNDe4cM3jSVIhshZ_Ag42KmRvuVSSTHDnWJo_QRiPQ_OxOa1rIiKlQG9jyq8eh0_sxcj3ODNZIYr1OPU4YZe3W3SBFfItGiOfmAAAAAGTFHWXAA",
)

SERVER_URL = genv("SERVER_URL", "https://heartxscrapper.koyeb.app/")


RSS_CHAT = int(
    genv("RSS_CHAT", "-1002426963681")
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
