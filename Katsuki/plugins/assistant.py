import config 
import asyncio

from pyrogram import filters, enums
from Katsuki import app, katsuki_info , katsuki 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


USERS = []

@app.on_message(filters.command("start") | filters.incoming  & filters.private)
async def start(_, message):
     user_id = message.from_user.id
     info = await katsuki_info()
     name = info.first_name
     id = info.id
     if user_id in USERS:
         return await message.reply("DON'T SPAM HERE!")
     USERS.append(user_id)
     await message.forward(config.LOG_GROUP_ID)
     mention = f"[{name}](tg://user?id={id})"
     BUTTON=InlineKeyboardMarkup([[
     InlineKeyboardButton("Source 👾", url=config.SOURCE),]])
     return await message.reply_text(f"""\n
Hello, I am Assistant for **{mention}**
You can deploy Your Own, To Use Me.
""",quote=True, reply_markup=BUTTON ,parse_mode=enums.ParseMode.MARKDOWN)
     await asyncio.sleep(10)
     USERS.remove(user_id)
     return 
