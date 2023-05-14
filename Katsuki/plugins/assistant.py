import config, strings
import asyncio

from pyrogram import filters, enums
from Katsuki import bot, INFO , app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


SPAM = []

@bot.on_message(filters.command("start") & filters.private)
async def start(_, message):
     user_id = message.from_user.id
     info = await INFO.app()
     name = info.first_name
     id = info.id
     if user_id in SPAM:
         return await message.reply("DON'T SPAM HERE!")
     SPAM.append(user_id)
     await message.forward(config.GROUP_ID)
     mention = f"[{name}](tg://user?id={id})"
     BUTTON=InlineKeyboardMarkup([[
     InlineKeyboardButton("Source 👾", url=config.SOURCE),]])
     return await message.reply_text(text=strings.BOT_START,quote=True, reply_markup=BUTTON ,parse_mode=enums.ParseMode.MARKDOWN)
     await asyncio.sleep(5)
     SPAM.remove(user_id)
     return 
