


"""
Copyright © [2023-2024] @NandhaBots. All rights reserved. Reproduction, modification, distribution, or republication of this file without prior written permission from @NandhaBots is strictly prohibited. The Katsuki Telegram user bot has been developed with the Pyrogram library and utilizing Python programming language, making it a safe and secure option for users. Unauthorized use of this bot or any part of it may result in legal action. This project is owned by @Nandha, and any unauthorized use or distribution of this bot is strictly prohibited.
"""


import config 
import requests


from nandha import MODULE, bot, lang
from nandha.helpers.inline_help import (
inline_paste, inline_fonts, inline_sof)
from nandha.helpers.misc import article

from pyrogram import filters
from pyrogram.types import (
InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton )



error_img = 'https://graph.org/file/6248cbb1e09af24a646f4.jpg'


BUTTONS = [[
InlineKeyboardButton('SOF', switch_inline_query_current_chat='sof text'),
InlineKeyboardButton('FONTS', switch_inline_query_current_chat='fonts text'),
InlineKeyboardButton('PASTE', switch_inline_query_current_chat='paste text'),     
 
]]



@bot.on_inline_query()
async def my_inline(_, inline_query):
     query = inline_query.query
     OWNER_ID = config.OWNER_ID  
     inline_query_id = inline_query.id
     
     if len(query) == 0:
           results = await article('Inline Commands', "**Here some commands**", 'https://graph.org/file/e2e4bdc46a616f46361ae.jpg', keyboard=InlineKeyboardMarkup(BUTTON))
           await bot.answer_inline_query(
                  inline_query_id, results, cache_time=1)   
          
     elif query.split()[0] == 'help':
          user_id = config.OWNER_ID
          if not inline_query.from_user.id == user_id:
                  return  
     
          buttons = [[InlineKeyboardButton(x['module'], callback_data=f"help:{x['module']}")] for x in MODULE]
          try:
              results = await article(lang['help_cmds'], lang['help_cmds'], 'https://graph.org/file/d71ae8adaac9ad004b3ca.jpg', InlineKeyboardMarkup(buttons))
              
              await bot.answer_inline_query(
                   inline_query_id,results,
                   cache_time=1,
              
              )
          except Exception as e:
                  results = await article('ERROR 404',
                        lang['error'].format(e), error_img)
                                    
                  await bot.answer_inline_query(
                 inline_query_id,results,
               cache_time=1,
              
          )
         
     elif query.split()[0] == 'paste':
             await inline_paste(bot, inline_query_id, query)
          
     elif query.split()[0] == 'fonts':
             await inline_fonts(bot, inline_query_id, query)
          
     elif query.split()[0] == 'sof':
             await inline_sof(bot, inline_query_id, query)
         
                   
            
             
             

 
