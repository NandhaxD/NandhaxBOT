
"""
Copyright © [2023-2024] @NandhaBots. All rights reserved. Reproduction, modification, distribution, or republication of this file without prior written permission from @NandhaBots is strictly prohibited. The Katsuki Telegram user bot has been developed with the Pyrogram library and utilizing Python programming language, making it a safe and secure option for users. Unauthorized use of this bot or any part of it may result in legal action. This project is owned by @Nandha, and any unauthorized use or distribution of this bot is strictly prohibited.
"""



import config, strings
import asyncio

from pyrogram import filters, enums
from Katsuki import bot, INFO , app
from Katsuki.helpers.help_func import emoji_convert
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


SPAM = []

@bot.on_message(filters.command("start") & filters.private)
async def start(_, message):
     user_id = message.from_user.id
     if user_id in SPAM:
         return await message.reply("`DON'T SPAM HERE!`")
     info = await INFO.app()
     botlive = await emoji_convert(bot.is_connected)
     applive = await emoji_convert(app.is_connected)
     name = info.first_name
     id = info.id
     SPAM.append(user_id)
     await message.forward(config.GROUP_ID)
     mention = f"[{name}](tg://user?id={id})"
     BUTTON=InlineKeyboardMarkup([[
     InlineKeyboardButton("SOURCE 👾", url=config.SOURCE),]])
     await message.reply_text(text=strings.BOT_START_STRING.format(mention=mention, applive=applive, botlive=botlive),quote=True, reply_markup=BUTTON ,parse_mode=enums.ParseMode.MARKDOWN)
     await asyncio.sleep(10)
     SPAM.remove(user_id)
     
