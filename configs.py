from os import getenv as genv
from pyrogram import Client

API_ID = genv("API_ID", "22977776")

API_HASH = genv("API_HASH", "2ac7223d720bdeec757cbc88ced57224")

BOT_TOKEN = genv("BOT_TOKEN", "7692272341:AAEcqZkFIx6Y6iljv96xt3SXSNwGY4_V8O4")

SUPPORT_GROUP = genv("SUPPORT_GROUP", "TGHelpingGroup")

UPDATES_CHANNEL = genv("UPDATES_CHANNEL", "PlayTamilX")

GROUP_ID = int(genv("GROUP_ID", "-1002341945360"))  # add group id where your leech is added

DATABASE_URL = genv(
    "DATABASE_URL",
    "mongodb+srv://jeevanantham8157:1055221@leechbot.gpkuo.mongodb.net/?retryWrites=true&w=majority&appName=Leechbot",
)

USER_SESSION_STRING = genv(
    "USER_SESSION_STRING",
    "BQFenPAAj0vR59QL_tH7p95B26NNPgETKPYRFf8jKfxPt2_rVChFajjDhjX101ZWItMub9Yo97IWN99spQoJ_ZkBjPxiyZJsSSX_AFrdbrdPitpEc8-NBul23Pz-j2Oo4Xw0i17iTnSf2oN0XnIYxh7VIkyB53ZR2UJErrAIvmkU9Im8on4rfifSyK1iXvRWIVFPs6e2Jc3xPGX_gMv6GOsLwb9y6cZ6Hni_uCrYbrV-A0rDgpmaa6kJXNOb54CT2FK7W275YYA8o2HdvXQlDmmKZpdtrjs6ekLdEcTv8Sbr-EhD4XEYqg86AcDPWrDOiXrLLr3EfKkRYu_E5Gwq4eEt05hzUQAAAAGTFHWXAA",
)

SERVER_URL = genv("SERVER_URL", "")


RSS_CHAT = int(
    genv("RSS_CHAT", "-1002335041395")
)  # add the channel id where the torrent files need to be sent

BASE_URL = genv(
    "BASE_URL", "https://www.1tamilmv.wf"
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

Updates - ⍟ @MadxBotz"""

ABOUT_TXT = """<b>╔════❰ Tʙ Sʜᴏʀᴛɴᴇʀ Bᴏᴛ ❱═══❍
║ ┏━━━━━━━━━❥
║ ┣ Mʏ ɴᴀᴍᴇ -> {}
║ ┣ Uᴘᴅᴀᴛᴇꜱ -> <a href="tg://TamilXLeech">••Bᴏᴛs••</a>
║ ┣ 𝖲ᴜᴘᴘᴏʀᴛ -> <a href="tg://TGHelpingGroup"> Bᴏᴛs Sᴜᴩᴩᴏʀᴛ</a>
║ ┣ ๏ Cʜᴇᴄᴋ ʜᴇʟᴘ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ.
║ ┗━━━━━━━━━❥
╚═════❰ @ ❱═════❍</b>"""


RELEASES_PATH = genv("RELEASES_PATH", "/index.php?/forums/topic/")  # dont change this
