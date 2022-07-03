import time 
import random 
from config import HANDLER, OWNER_ID, KATSUKI, ALIVE_TEXT
from pyrogram import filters, __version__ as pyrover
from Katsuki import katsuki, get_readable_time, StartTime

you = katsuki.get_me()

@katsuki.on_message(filters.command("alive",prefixes=HANDLER) & filters.user(OWNER_ID))
async def alive(_, m):
    start_time = time.time()
    end_time = time.time()
    ping_time = round((end_time - start_time) * 1000, 3)
    uptime = get_readable_time((time.time() - StartTime))
    await m.reply_photo(random.choice(KATSUKI),caption=ALIVE_TEXT.format(you.mention,pyrover,ping_time,uptime))

      
