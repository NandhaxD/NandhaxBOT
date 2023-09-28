
"""
Copyright © [2023-2024] @NandhaBots. All rights reserved. Reproduction, modification, distribution, or republication of this file without prior written permission from @NandhaBots is strictly prohibited. The Katsuki Telegram user bot has been developed with the Pyrogram library and utilizing Python programming language, making it a safe and secure option for users. Unauthorized use of this bot or any part of it may result in legal action. This project is owned by @Nandha, and any unauthorized use or distribution of this bot is strictly prohibited.
"""



from Katsuki import app
from Katsuki.helpers.help_func import FileType
import config
import os
from pyrogram import filters

THUMB_ID = "./IMG_20220701_185623_542.jpg"

async def FileType(message):
    if message.document:
        type = message.document.mime_type
        return ["txt" if type == "text/plain" else type.split("/")[1]][0]
    elif message.photo:
          return "jpg"
    elif message.animation:
          return message.animation.mime_type.split("/")[1]
    elif message.video:
         return message.video.mime_type.split("/")[1]
    else:
         return False
        



@app.on_message(filters.command("rename",prefixes=config.HANDLER) & filters.me)
async def rename(_, message):
    try:
       filename = message.text.split(None,1)[1]
    except:
        name = config.NAME
        try:
          if (await FileType(message=message.reply_to_message)) != False:
               filetype = await FileType(message=message.reply_to_message)
        except Exception as e:
               return await message.reply_text(f"Error: `{e}`")
        filename = "{name}.{filetype}".format(name=name, filetype=filetype)
    msg = await message.edit("⬇️ File has downloading...")
    path = await message.reply_to_message.download(file_name=filename)
    await msg.edit_text("⬆️ File has uplaoding")
    await message.reply_document(document=path, thumb=THUMB_ID, quote=True)
    await msg.delete()
    os.remove(path)
    return 
    
    
    
