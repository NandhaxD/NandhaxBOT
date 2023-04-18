import time 
import random 
from config import HANDLER, OWNER_ID, KATSUKI, ALIVE_TEXT
from pyrogram import filters, __version__ as pyrover
from Katsuki import katsuki, get_readable_time, StartTime


@katsuki.on_message(filters.command("alive",prefixes=HANDLER) & filters.user(OWNER_ID))
async def alive(_, message):
    name = (await katsuki.get_me()).first_name
    uptime = get_readable_time((time.time() - StartTime))
    alive = await message.reply_animation(KATSUKI, caption="")
    await alive.edit_caption(f"Hello, **{name}**,\nYou Are Using Katsuki UB,\nCurrent Pyrogram Version {pyroved}, I Awake on {uptime}!")

katsuki.on_message(filters.command("ping",prefixes=HANDLER) & filters.user(OWNER_ID))
async def ping(_, message):
     start_time = time.time()
     end_time = time.time()
     ping_time = round((end_time - start_time) * 1000, 3)
     await message.edit(f"🔔 pong: {ping_time}")

