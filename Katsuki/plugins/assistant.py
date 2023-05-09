from pyrogram import filters, enums
from Katsuki import app, katsuki, mention 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@app.on_message(filters.command("start") & filters.private)
async def start(_, message):
     MENTION = await mention()
     BUTTON=InlineKeyboardMarkup([[
     InlineKeyboardButton("Source 👾", url="https://github.com/nandhaxd/Katsuki"),]])
     return await message.reply_text(f"""\n
Hello, I am Assistant for **{MENTION}**
You can deploy Your Own, To Use Me.""",quote=True, reply_markup=BUTTON ,parse_mode=enums.ParseMode.MARKDOWN)
