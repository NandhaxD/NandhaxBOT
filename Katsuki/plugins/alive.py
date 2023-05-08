import time 
import config
import strings
from pyrogram import filters, __version__ as pyrover, enums
from Katsuki import katsuki, StartTime
from Katsuki.katsuki_help.help_func import get_readable_time, alive_edit_message





@katsuki.on_message(filters.command(["alive","live"], prefixes=config.HANDLER) & filters.user(config.OWNER_ID))
async def alive(_, message):
     animation=config.KATSUKI
     name=strings.BIG_NAME
     mention=f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
     caption=f"""\n
     {name}

Greetings, Master {mention}! 
I, Katsuki, am an anime-themed user bot
who possesses an abundance of commands at your service. 
Let me aid you in your endeavors with my unique skills and abilities. Together, 
we shall conquer the digital universe!

> Live Pyrogram Version is {pyrover}
"""    
     if message.reply_to_message:
          return await message.reply_to_message.reply_animation(animation=animation, quote=True, caption=caption, parse_mode=enums.ParseMode.MARKDOWN)
     return await message.reply_animation(animation=animation, quote=True, caption=caption, parse_mode=enums.ParseMode.MARKDOWN)
   

@katsuki.on_message(filters.command("ping",prefixes=config.HANDLER) & filters.user(config.OWNER_ID))
async def ping(_, message):
     start_time = time.time()
     end_time = time.time()
     ping_time = round((end_time - start_time) * 1000, 5)
     uptime = get_readable_time((time.time() - StartTime))
     string=f"**S Y S T E M**:\n=> **Pong**: {ping_time}\n=> **Uptime**: {uptime}"
     if message.reply_to_message:
          return await message.reply_to_message.reply_text(text=string, quote=True, parse_mode=enums.ParseMode.MARKDOWN)
     return await message.reply_text(text=string, quote=True, parse_mode=enums.ParseMode.MARKDOWN)
   
