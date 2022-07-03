import random 
import asyncio
from config import HANDLER, OWNER_ID, KATSUKI, ALIVE_TEXT
from pyrogram import filters, __version__ as lol
from pyrogram.types import Message
from Katsuki import katsuki, you
from platform import python_version as pyver

___version___ = "0.1.0"
      
@katsuki.on_message(filters.command("alive",prefixes=HANDLER) & filters.user(OWNER_ID))
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("⚡")
    await asyncio.sleep(1)
    await accha.edit("ᴀʟɪᴠɪɴɢ..")
    await asyncio.sleep(0.1)
    await accha.edit("ᴀʟɪᴠɪɴɢ...")
    await accha.delete()
    await asyncio.sleep(0.1)
    umm = await m.reply_sticker("CAACAgUAAx0CachlIwABBRm8Yrh0oK50UFlHP-z3nZwnGMZvlicAArIDAAJUc9lXWW-s0PALuYIpBA")
    await umm.delete()
    await asyncio.sleep(0.1)
    await m.reply_photo(
        random.choice(KATSUKI),
        caption=f"""
        ━━━━━━━━━━━━━━━━━━━
        ► **ʏᴀᴀ ᴀᴍ ᴀʟɪᴠᴇ ʀᴇᴀᴅʏ ᴛᴏ ʀᴏᴄᴋ**
        
        ► **ᴏᴡɴᴇʀ :** [{you.first_name}](https://t.me/{you.id})
        
        ► **ᴍᴇᴛᴀ ᴠᴇʀsɪᴏɴ :** `{___version___}`
        
        ► **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{lol}`
        
        ► **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{pyver()}`
        
        **[sᴜᴘᴘᴏʀᴛ](https://t.me/Katsuki_Support)|[ᴜᴘᴅᴀᴛᴇs](https://t.me/Katsuki_Updates)**
        ━━━━━━━━━━━━━━━━━
        """,
    )      
      
