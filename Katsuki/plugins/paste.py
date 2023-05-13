import strings
import requests 
import config, os
import datetime

from Katsuki import katsuki
from Katsuki.helpers.help_func import spacebin, convert_to_datetime
from pyrogram import filters, enums




 

  
    

@katsuki.on_message(filters.command("paste",config.HANDLER) & filters.user(config.OWNER_ID))
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
          return await message.edit(strings.PAST_FORMAT.format(link=link, raw=raw,timedate=timedate), parse_mode=enums.ParseMode.MARKDOWN, disable_web_page_preview=True)

    elif (message.reply_to_message.document and bool(message.reply_to_message.document.mime_type.startswith("text/"))):
           path = await katsuki.download_media(message.reply_to_message)
           file = open(path, "r")
           text = file.read()
           file.close()
           os.remove(path)

           mm = await spacebin(text)
           timedate = await convert_to_datetime(mm["result"]["datetime"])
           link = mm["result"]["link"]
           raw = mm["result"]["raw"]

           return await message.edit(strings.PAST_FORMAT.format(link=link, raw=raw,timedate=timedate), parse_mode=enums.ParseMode.MARKDOWN, disable_web_page_preview=True)

    elif bool(message.reply_to_message.text or message.reply_to_message.caption):


           if message.reply_to_message.text:
                 text = message.reply_to_message.text
           elif message.reply_to_message.caption:
                 text = message.reply_to_message.caption
        
           mm = await spacebin(text)
           timedate = await convert_to_datetime(mm["result"]["datetime"])
           link = mm["result"]["link"]
           raw = mm["result"]["raw"]

           return await message.edit(strings.PAST_FORMAT.format(link=link, raw=raw,timedate=timedate), parse_mode=enums.ParseMode.MARKDOWN, disable_web_page_preview=True)
    else:
         return await message.edit("=> I am unable to paste this.")



        
    
