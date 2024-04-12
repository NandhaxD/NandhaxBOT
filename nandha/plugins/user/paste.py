
"""
Copyright © [2023-2024] @NandhaBots. All rights reserved. Reproduction, modification, distribution, or republication of this file without prior written permission from @NandhaBots is strictly prohibited. The Katsuki Telegram user bot has been developed with the Pyrogram library and utilizing Python programming language, making it a safe and secure option for users. Unauthorized use of this bot or any part of it may result in legal action. This project is owned by @Nandha, and any unauthorized use or distribution of this bot is strictly prohibited.
"""




import requests 
import config, os

from nandha import app, lang
from nandha.helpers.help_func import spacebin, convert_to_datetime
from pyrogram import filters, enums


  
    

@app.on_message(filters.command("paste",config.PREFIXES) & filters.me)
async def paste(_, message):
    #share your codes on https://spacebin.in

    if not message.reply_to_message:
          try:
              text = message.text.split(None,1)[1]
          except:
               await message.edit("=> Input text to paste else reply.")
               return           
          mm = await spacebin(text)
          timedate = await convert_to_datetime(mm["result"]["datetime"])
          link = mm["result"]["link"]
          raw = mm["result"]["raw"]          
          return await message.edit(lang['paste'].format(link, raw, timedate), parse_mode=enums.ParseMode.MARKDOWN, disable_web_page_preview=True)

    elif (message.reply_to_message.document and bool(message.reply_to_message.document.mime_type.startswith("text/"))):
           path = await app.download_media(message.reply_to_message)
           file = open(path, "r")
           text = file.read()
           file.close()
           os.remove(path)

           mm = await spacebin(text)
           timedate = await convert_to_datetime(mm["result"]["datetime"])
           link = mm["result"]["link"]
           raw = mm["result"]["raw"]

           return await message.edit(lang['paste'].format(link, raw, timedate), parse_mode=enums.ParseMode.MARKDOWN, disable_web_page_preview=True)

    elif bool(message.reply_to_message.text or message.reply_to_message.caption):
           if message.reply_to_message.text:
                 text = message.reply_to_message.text
           elif message.reply_to_message.caption:
                 text = message.reply_to_message.caption
        
           mm = await spacebin(text)
           timedate = await convert_to_datetime(mm["result"]["datetime"])
           link = mm["result"]["link"]
           raw = mm["result"]["raw"]

           return await message.edit(lang['paste'].format(link, raw, timedate), parse_mode=enums.ParseMode.MARKDOWN, disable_web_page_preview=True)
    else:
         return await message.edit(lang['wrong'])


    
