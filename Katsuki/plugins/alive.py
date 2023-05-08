import time 
import config
import string
from pyrogram import filters, __version__ as pyrover
from Katsuki import katsuki, StartTime
from Katsuki.katsuki_help.help_func import get_readable_time, alive_edit_message





@katsuki.on_message(filters.command(["alive","live"], prefixes=config.HANDLER) & filters.user(config.OWNER_ID))
async def alive(_, message):
     animation=config.KATSUKI
     caption=string.KATSUKI_BIG_NAME
     if message.reply_to_message:
          return await message.reply_to_message.reply_animation(animation=animation, quote=True)
     return await message.reply_animation(animation=animation, quote=True)
   

@katsuki.on_message(filters.command("ping",prefixes=config.HANDLER) & filters.user(config.OWNER_ID))
async def ping(_, message):
     start_time = time.time()
     end_time = time.time()
     ping_time = round((end_time - start_time) * 1000, 3)
     uptime = get_readable_time((time.time() - StartTime))
     await message.edit(f"**S Y S T E M**:\n=> **Pong**: {ping_time}\n=> **Uptime**: {uptime}")

