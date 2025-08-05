from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from configs import *
from plugins.commands import user_pagination, show_document

@Client.on_callback_query()
async def callback(bot, query):
    me = await bot.get_me()
    data = query.data
    msg = query.message

    if data == "delete":
        await msg.delete()
        try:
            await msg.reply_to_message.delete()
        except:
            pass
                    
    elif data.startswith("prev_") or data.startswith("next_"):
        _, user_id, current_index = data.split("_")
        current_index = int(current_index)

        await show_document(bot, msg, int(user_id), current_index)
            
            
    elif data == "help":
        await msg.edit(
            HELP_TXT.format(me.mention),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Aʙᴏᴜᴛ ★", callback_data="about"),
                        InlineKeyboardButton(
                            "Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ ⌘", url="https://t.me/MKxSupport_Group"
                        ),
                    ],
                    [InlineKeyboardButton("Bᴀᴄᴋ 𖦹", callback_data="start")],
                ]
            ),
        )

    elif data == "about":
        await msg.edit(
            ABOUT_TXT.format(me.mention),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Sᴏᴜʀᴄᴇ Cᴏᴅᴇ 😎", url="https://t.me/Monster_Mk_Bot"
                        ),
                        InlineKeyboardButton(
                            "Uᴘᴅᴀᴛᴇs ⚡", url="https://t.me/MKxBoTz"
                        ),
                    ],
                    [InlineKeyboardButton("Bᴀᴄᴋ 𖦹", callback_data="start")],
                ]
            ),
        )


    elif data == "start":
        await msg.edit(
            START_TXT.format(query.from_user.mention),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Bᴏᴛ Sᴇᴛᴛɪɴɢs ⚙️", callback_data="help"),
                    ],
                    [
                        InlineKeyboardButton(
                            "Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ 💢", url=f"https://t.me/MKxSupport_Group"
                        ),
                        InlineKeyboardButton(
                            "Dᴇᴠᴇʟᴏᴘᴇʀ 👨‍💻", url=f"https://t.me/Monster_Mk_Bot"
                        ),
                    ],
                    [InlineKeyboardButton("✇ Jᴏɪɴ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ ✇", url=f"https://t.me/MKxBoTz")],
                ]
            ),
        )
