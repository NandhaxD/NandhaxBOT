import random 
from config import HANDLER, OWNER_ID, KATSUKI, ALIVE_TEXT
from pyrogram import filters
from pyrogram.types import Message
from Katsuki import katsuki
from platform import python_version as pyver
      
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
        caption=ALIVE_TEXT,
    )      
      
