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
    "BQFenPAAdeKaSkO4rJKrRtVppDnDzTgX1yDSk8El1s8dB8LsffWMHy8CGgoLmkv5ulyV4xHdFGwba0LufbE0qJQxFfvg8Ydz1yZvGgdhy5eUmfO7FyDpr9fdxXbq0j3MAgJbbWGla_ulnoMYcMj6aakKyOQbzzRIhF157FdfD3XmoG3YtEIixJn5vqxiqFyaxDq2wJAyUVip1vXqaCEukmkj02o43MysmlMH3BfOGHgDaWMv1BJGPALfZLZF0uBPSNgXiZxzTF3nQHcIbes-wcK1wbwIoGYaBHLxv13OZzRp_SBAaZfwlR3Er6mJF7Y32iz4u9KcD445ijYCoWtw3XGy0mguMAAAAAGTFHWXAA",
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
