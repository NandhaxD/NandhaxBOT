


"""
Copyright © [2023-2024] @NandhaBots. All rights reserved. Reproduction, modification, distribution, or republication of this file without prior written permission from @NandhaBots is strictly prohibited. The Katsuki Telegram user bot has been developed with the Pyrogram library and utilizing Python programming language, making it a safe and secure option for users. Unauthorized use of this bot or any part of it may result in legal action. This project is owned by @Nandha, and any unauthorized use or distribution of this bot is strictly prohibited.
"""


import config 
import requests


from nandha import MODULE, bot, lang
from nandha.helpers.help_func import spacebin
from pyrogram import filters

from pyrogram.types import (
InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton )




async def inline_paste(bot, inline_query):
    context = inline_query.query.split(None, 1)[1]
    paste = await spacebin(context)
    link = ['result']['link']
    raw = ['result']['raw']
    datetime = ['result']['datetime']
    try:
         await bot.answer_inline_query(
                 inline_query.id,
               cache_time=1,
              results=[
                    InlineQueryResultArticle(
                   "Click Here",
                     InputTextMessageContent(
                message_text=lang['paste'].format(link, raw, datetime),
                               disable_web_page_preview=True), thumb_url="https://telegra.ph/file/bea4f6c85c9dc5773521e.jpg")])
    except Exception as e:
            await bot.answer_inline_query(
                 inline_query.id,
               cache_time=1,
              results=[
                    InlineQueryResultArticle(
                   "Click Here",
                     InputTextMessageContent(
                message_text=['error'].format(e),
                               disable_web_page_preview=True), thumb_url="https://telegra.ph/file/e20ed7b575028c62e5bf1.jpg")])
    
  



@bot.on_inline_query()
async def my_inline(_, inline_query):
     query = inline_query.query.lower()
     OWNER_ID = config.OWNER_ID  
     if len(query) == 0:
           string = inline_query
           await bot.answer_inline_query(
                  inline_query.id,
                  cache_time=1,
                    results=[
                    InlineQueryResultArticle(
                   "Here available commands for free uses.",
                     InputTextMessageContent(
                message_text=string,
                               disable_web_page_preview=True), thumb_url="https://telegra.ph/file/94a1e1e74fa5dcc631f62.jpg")])
     
         
     elif query == 'help':
          user_id = config.OWNER_ID
          if not inline_query.from_user.id == user_id:
                  return  
     
          buttons = [[InlineKeyboardButton(x['module'], callback_data=f"help:{x['module']}")] for x in MODULE]
          try:
              await bot.answer_inline_query(
                   inline_query.id,
                   cache_time=1,
                   results = [
                         InlineQueryResultArticle(
                         lang['help_cmds'],  InputTextMessageContent(message_text=lang['help_cmds']), thumb_url="https://graph.org/file/d71ae8adaac9ad004b3ca.jpg",reply_markup=InlineKeyboardMarkup(buttons))])
          except Exception as e:
                  await bot.answer_inline_query(
                        inline_query.id,
                        cache_time=0,
                              results = [
                             InlineQueryResultArticle(
                         lang['help_cmds'],  InputTextMessageContent(message_text=lang['error'].format(e)), thumb_url="https://graph.org/file/d71ae8adaac9ad004b3ca.jpg",reply_markup=InlineKeyboardMarkup(buttons))])
            
     elif query == 'paste':
             await inline_paste(bot, inline_query)
             
             
             

 
