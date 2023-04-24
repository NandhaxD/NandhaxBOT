import requests 
import config, os
import datetime

from Katsuki import katsuki
from pyrogram import filters



async def convert_to_datetime(timestamp): # Unix timestamp
     date = datetime.datetime.fromtimestamp(timestamp)
     return date


async def spacebin(text: str):
    url = "https://spaceb.in/api/v1/documents/"
    response = requests.post(url, data={"content": text, "extension": "txt"})
    id = response.json().get('payload').get('id')
    response = requests.get("https://spaceb.in/api/v1/documents/{id}").json()
    content = response.get("payload").get("content")
    created_at = response.get("payload").get("created_at")
    link = f"https://spacebin.in/{id}"
    raw = f"https://spaceb.in/api/v1/documents/{id}/raw"
    datetime = await convert_to_datetime(created_at)
    string = f"""\u0020
**Here's the link**: **[Paste link]({link})**
**Here's the link**: **[Raw View]({raw})**
**Created at: {datetime}
"""
    return string

    
    
    



@katsuki.on_message(filters.command("paste",config.HANDLER) & filters.user(config.OWNER_ID))
async def paste(_, message):
    #share your codes on https://spacebin.in
    if not message.reply_to_message:
          try:
              text = message.text.split(None,1)[1]
          except:
               await message.edit("=> Input text to paste else reply.")
               return 

          link = await spacebin(text)
          return await message.edit(link)

    elif bool(message.reply_to_message.text or message.reply_to_message.caption):
         
           if message.reply_to_message.text:
                 text = message.reply_to_message.text
           elif message.reply_to_message.caption:
                 text = message.reply_to_message.caption
        
           link = await spacebin(text)
           return await message.edit(link)

    elif bool(message.reply_to_message.document.mime_type.startswith("text/")):
           path = await katsuki.download_media(message.reply_to_message)
           file = open(path, "r")
           text = file.read()
           file.close()
           os.remove(path)
           link = await spacebin(text)
           return await message.edit(link)
    else:
         return await message.edit("=> I am unable to paste this.")



        
    
