from pyrogram import filters, enums
from Katsuki import app, katsuki_info , mention 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


"""
@app.on_message(filters.command("start") & filters.private)
async def start(_, message):
     info = await katsuki_info()
     name = info.first_name
     id = info.id
     mention = "[{name}](tg://user?id={id})"
     BUTTON=InlineKeyboardMarkup([[
     InlineKeyboardButton("Source 👾", url="https://github.com/nandhaxd/Katsuki"),]])
     #return await message.reply_text(f"""\n
Hello, I am Assistant for **{mention}**
You can deploy Your Own, To Use Me.
#""",quote=True, reply_markup=BUTTON ,parse_mode=enums.ParseMode.MARKDOWN)
"""
