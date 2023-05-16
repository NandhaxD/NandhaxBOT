
"""
Copyright © [2023-2024] @NandhaBots. All rights reserved. Reproduction, modification, distribution, or republication of this file without prior written permission from @NandhaBots is strictly prohibited. The Katsuki Telegram user bot has been developed with the Pyrogram library and utilizing Python programming language, making it a safe and secure option for users. Unauthorized use of this bot or any part of it may result in legal action. This project is owned by @Nandha, and any unauthorized use or distribution of this bot is strictly prohibited.
"""



import strings

from Katsuki import bot, MODULE, INFO as GET_INFO
from pyrogram import filters, enums 

from pyrogram.types import ( 
InlineKeyboardMarkup, InlineKeyboardButton )


@bot.on_callback_query(filters.regex("help_back"))
async def help_back(_, query):
   user_id = (await GET_INFO.app()).id
   if not query.from_user.id == int(user_id):
       return await query.answer("😤 You aren't my master")
   buttons = [[InlineKeyboardButton(x['module'], callback_data=f"help:{x['module']}")] for x in MODULE]
   return await bot.edit_inline_text(
       inline_message_id=query.inline_message_id, text="[`HELP COMMANDS`]", reply_markup=InlineKeyboardMarkup(buttons), parse_mode=enums.ParseMode.MARKDOWN)
       
     

@bot.on_callback_query(filters.regex('^help'))
async def help_commnds(_, query):
   user_id = (await GET_INFO.app()).id
   if not query.from_user.id == int(user_id):
       return await query.answer("😤 You aren't my master")
   CB_NAME = query.data.split(':')[1].casefold()
   data = [x for x in MODULE if x['module'].casefold() == CB_NAME]
   if len(data) == 0:
       return await query.answer("🤔 somthing wrong.")
   module = data[0]['module']
   help = data[0]['help']
   button = InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ BACK",callback_data="help_back")]])
   return await bot.edit_inline_text(inline_message_id=query.inline_message_id, text=strings.HELP_CMD.format(module=module, help=help), parse_mode=enums.ParseMode.MARKDOWN, reply_markup=button)
       
            
            

   
