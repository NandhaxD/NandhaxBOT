import time 
import random 
import asyncio
from config import HANDLER, OWNER_ID, KATSUKI, ALIVE_TEXT
from pyrogram import filters, __version__ as pyrover
from Katsuki import katsuki, get_readable_time, StartTime


@katsuki.on_message(filters.command("alive",prefixes=HANDLER) & filters.user(OWNER_ID))
async def alive(_, message):
    name = (await katsuki.get_me()).first_name
    alive = await message.reply_animation(KATSUKI, caption="")
    string = name.split()
    caption = ""
    for x in string:
         caption += x
         await asyncio.sleep(3)
         await alive.edit_caption(caption)
    await alive.edit_caption(f"Hello Master, **{name}**,\nYou Are Using Katsuki And Your Current Pyrogram Version is {pyrover}!")


@katsuki.on_message(filters.command("ping",prefixes=HANDLER) & filters.user(OWNER_ID))
async def ping(_, message):
     start_time = time.time()
     end_time = time.time()
     ping_time = round((end_time - start_time) * 1000, 3)
     uptime = get_readable_time((time.time() - StartTime))
     await message.edit(f"👾 **System uptime & ping**\n🔔 **Pong**: {ping_time}\n⬆️ **Uptime**: {uptime}")

