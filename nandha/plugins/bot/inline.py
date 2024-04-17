


"""
Copyright © [2023-2024] @NandhaBots. All rights reserved. Reproduction, modification, distribution, or republication of this file without prior written permission from @NandhaBots is strictly prohibited. The Katsuki Telegram user bot has been developed with the Pyrogram library and utilizing Python programming language, making it a safe and secure option for users. Unauthorized use of this bot or any part of it may result in legal action. This project is owned by @Nandha, and any unauthorized use or distribution of this bot is strictly prohibited.
"""


import config 
import requests

from urllib.parse import quote
from nandha import MODULE, bot, lang
from nandha.helpers.help_func import spacebin
from pyrogram import filters

from pyrogram.types import (
InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton )


api_url = 'https://nandha-api.onrender.com/'
error_img = 'https://graph.org/file/6248cbb1e09af24a646f4.jpg'



async def article(name: str, article: str, thumb_url: str , keyboard: str = None):     
     results=[
         InlineQueryResultArticle(
                   name,
                     InputTextMessageContent(
                message_text=article,
                               disable_web_page_preview=True), 
             thumb_url=thumb_url, 
             reply_markup=keyboard)
     ]
     return results
    

async def inline_paste(bot, inline_query_id, context):
    try:
        paste = await spacebin(context)
        link = paste['result']['link']
        raw = paste['result']['raw']
        datetime = paste['result']['datetime']
        name = 'Here your paste'
        results = await article(
            name, lang['paste'].format(link, raw, datetime), 'https://graph.org/file/d7ee801a941e632db40f1.jpg')
        
        await bot.answer_inline_query(
                 inline_query_id, results,
               cache_time=1 )
    except Exception as e:
            results = await article('ERROR 404',
                        lang['error'].format(e), error_img)
                                    
            await bot.answer_inline_query(
                 inline_query_id,results,
               cache_time=1
              
            )
    
  


async def inline_fonts(bot, inline_query_id, context):
            try:
                end_point = f'styletext?query={quote(context)}'
                req = requests.get(api_url+end_point).json()
                context = f"**Query**: {context}\n\n"
                for text in req['fonts']:
                       context += text+"\n"
                results = await article('Style Fonts', context, 'https://graph.org/file/d95f726d8fe3706cc69ae.jpg')
                await bot.answer_inline_query(
                      inline_query_id,results,
                             cache_time=1,
                          
                         )
            except Exception as e:
                    results = await article('ERROR 404',
                        lang['error'].format(e), error_img)
                                    
                    await bot.answer_inline_query(
                 inline_query_id, results,
               cache_time=1,
              
                    )


@bot.on_inline_query()
async def my_inline(_, inline_query):
     query = inline_query.query
     OWNER_ID = config.OWNER_ID  
     inline_query_id = inline_query.id
     if len(query) == 0:
           string = inline_query
           results = await article('Objects', string, 'https://telegra.ph/file/94a1e1e74fa5dcc631f62.jpg')
           await bot.answer_inline_query(
                  inline_query_id,results,
                  cache_time=1,
                    
)
     
         
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
             context = query.split(None, 1)[1]
             await inline_paste(bot, inline_query_id, context)


     elif query.split()[0] == 'fonts':
            context = query.split(None, 1)[1]
            await inline_fonts(bot, inline_query_id, context)
          
                
         
                   
            
             
             

 
