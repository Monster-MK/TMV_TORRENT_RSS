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
    "BQFenPAAUpZm1YzhmQVuc-H2LjgYfks92YR7GpnF2Gisr_DpHFctvyUQOJ72TvwCBt_84Vpf5u9mV3rNfhgIyqGW7aQZoFCdWP57euJLMjp7pIgn5NeCR7aJYtUSmWgD76aadhibviZPWLvml2JA6pz1DbNKH6Qe4LsnL7LM7i1nSW3kWCXfxqxCfduBfXTbhr3r7QaNldIIPWXHkTbDe-fUNv3xlU3ewH1N3lJToyQWltxVaIV3zmNNEksULc8EE2OyfBU3WCBr7tJAg1-eqn-d7UzDnjXpmdK3rIiVstKwhxezty8CeRsml2qa2389W6CcXl0V0WLnBPLb_cjwoo1h8a0ABgAAAAGTFHWXAA",
)

SERVER_URL = genv("SERVER_URL", "https://heartxscrapper.koyeb.app/")


RSS_CHAT = int(
    genv("RSS_CHAT", "-1002426963681")
)  # add the channel id where the torrent files need to be sent

BASE_URL = genv(
    "BASE_URL", "https://www.1tamilmv.si"
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

ABOUT_TXT = """<b>╔════❰ HeartXBotz ❱═══❍
║ ┏━━━━━━━━━❥
║ ┣ Mʏ ɴᴀᴍᴇ -> {}
║ ┣ Uᴘᴅᴀᴛᴇꜱ -> <a href="tg://HeartXBotz">••Bᴏᴛs••</a>
║ ┣ 𝖲ᴜᴘᴘᴏʀᴛ -> <a href="tg://TGHelpingGroup"> Bᴏᴛs Sᴜᴩᴩᴏʀᴛ</a>
║ ┣ ๏ Cʜᴇᴄᴋ ʜᴇʟᴘ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ.
║ ┗━━━━━━━━━❥
╚═════❰ @ ❱═════❍</b>"""


WEEK_RELEASES_PATH = genv("RELEASES_PATH", "/index.php?/forums/topic/")  # dont change this
