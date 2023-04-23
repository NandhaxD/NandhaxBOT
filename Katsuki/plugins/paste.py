import requests 
import config, os

from Katsuki import katsuki
from pyrogram import filters


async def spacebin(text: str):
    url = "https://spaceb.in/api/v1/documents/"
    response = requests.post(url, data={"content": text, "extension": "txt"})
    link = f"https://spaceb.in/{response.json().get('payload').get('id')}"
    return link



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

    elif message.reply_to_message.document.mime_type.startswith("text/"):
           path = await katsuki.download_media(message.reply_to_message)
           file = open(path, "r")
           text = file.read()
           file.close()
           os.remove(path)
           link = await spacebin(text)
           return await message.edit(link)
    else:
         return message.edit("=> I cannot paste this.")



        
    
