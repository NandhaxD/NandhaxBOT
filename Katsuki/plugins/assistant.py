import config 

from pyrogram import filters, enums
from Katsuki import app, katsuki_info , katsuki 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


x = []

@app.on_message(filters.command("start") | filters.incoming  & filters.private)
async def start(_, message):
     info = await katsuki_info()
     name = info.first_name
     id = info.id
     if message.from_user.id in x:
         return await message.reply("DON'T SPAM HERE!")
     x.append(message.from_user.id)
     await message.forward(config.LOG_GROUP_ID)
     mention = "[{name}](tg://user?id={id})"
     BUTTON=InlineKeyboardMarkup([[
     InlineKeyboardButton("Source 👾", url="https://github.com/nandhaxd/Katsuki"),]])
     return await message.reply_text(f"""\n
Hello, I am Assistant for **{mention}**
You can deploy Your Own, To Use Me.
""",quote=True, reply_markup=BUTTON ,parse_mode=enums.ParseMode.MARKDOWN)
     await asyncio.sleep(20)
     x.remove(message.from_user.id)
     return 
