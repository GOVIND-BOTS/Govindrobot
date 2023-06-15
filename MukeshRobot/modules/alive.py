import asyncio
from platform import python_version as pyver

from pyrogram import __version__ as pver
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as lver
from telethon import __version__ as tver

from MukeshRobot import SUPPORT_CHAT, pbot,BOT_USERNAME, OWNER_ID

PHOTO = [
    "https://te.legra.ph/file/e1e8f294df0f0a4803dcc.jpg",
    "https://te.legra.ph/file/e1e8f294df0f0a4803dcc.jpg",
    "https://te.legra.ph/file/e1e8f294df0f0a4803dcc.jpg",
    "https://te.legra.ph/file/e1e8f294df0f0a4803dcc.jpg",
    "https://te.legra.ph/file/e1e8f294df0f0a4803dcc.jpg",
]

Mukesh = [
    [
        InlineKeyboardButton(text="❤️𝐎𝐖𝐍𝐄𝐑❤️‍🩹", url=f"tg://user?id=6099950428"),
        InlineKeyboardButton(text="🍒𝐆𝐑𝐎𝐔𝐏🍒", url=f"https://t.me/indian_chatting_club_offical"),
    ],
    [
        InlineKeyboardButton(
            text="☆ 𝐀𝐝𝐝 𝐌𝐞 𝐌𝐨𝐢 𝐋𝐮𝐯 ☆",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

lol = "https://te.legra.ph/file/e1e8f294df0f0a4803dcc.jpg"


@pbot.on_message(filters.command("alive"))
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("⚡")
    await asyncio.sleep(0.5)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ..")
    await asyncio.sleep(0.5)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ......")
    await asyncio.sleep(0.5)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ..")
    await asyncio.sleep(0.5)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ......")
    await accha.delete()
    await asyncio.sleep(0.5)
    umm = await m.reply_sticker(
        "AACAgUAAxkBAAIjTGKPYCq3keRZgNbshxtJ5k7H609OAAIZBgACYAF5VIerYoMcSln8JAQ"
    )
    await umm.delete()
    await asyncio.sleep(0.8)
    await m.reply_photo(
        lol,
        caption=f"""**🌷ʜᴇʏ, ɪ ᴀᴍ 『[𝗜𝗖𝗖 𝗥𝗢𝗕𝗢𝗧](f"t.me/{BOT_USERNAME}")』🎄**
   ╔═════ஜ۩۞۩ஜ════╗

   ♨️𝗠𝗔𝗗𝗘 𝗕𝗬 [𝗚𝗢𝗩𝗜𝗡𝗗](https://t.me/GOVIND_OFFICIAL_MP42)♨️

   ╚═════ஜ۩۞۩ஜ════╝""",
        reply_markup=InlineKeyboardMarkup(Mukesh),
    )
__mod_name__ = "♨️ᴀʟɪᴠᴇ♨️"
__help__ = """

*ᴜsᴇʀ ᴄᴏᴍᴍᴀɴᴅs*:
» /alive*:* ᴛᴏ ᴄʜᴇᴀᴋ ❓  ɪ ᴀᴍ ᴀʟɪᴠᴇ ᴏʀ ɴᴏᴛ?

☆............𝙱𝚈 » [𝗚𝗢𝗩𝗜𝗡𝗗](https://t.me/GOVIND_OFFICIAL_MP42)............☆"""
