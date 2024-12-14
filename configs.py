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
    "BQFenPAASdfpOmlYrWej_OFfcpKdr0GdpvKE8gJ2NOnCWTdIqPl1hi7N28ytJJhGEjTuuPrzW1zCAVDtW_v-VPTH0wz9p1gw4eMvsRWS-qQNRgzCS_P_G-vAoPYaWOY5fA_vkrFotvdFUwUgNH3G-y5nl_uxlSygPlwjNq5OYF0kE3DH7Lb9DGIzbivv1YCRUAJDZ3LE_rWkBAfBKHE7XAdPFV7-kf8egNBgkeVrUOPwUUwnmEwWzTN2OQkc1rduFNkuAsDuQ6vDaJg9zWhrhtwEScMraVnZ0QqkA-_VMutzaIpHw7MEr08SdXXl8yJOlrUsEOg5iqC1PdD_1vQWHl9hMYvfAwAAAAGTFHWXAA",
)

SERVER_URL = genv("SERVER_URL", "https://web-fp63vcz8q4vh.up-de-fra1-k8s-1.apps.run-on-seenode.com/")


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
