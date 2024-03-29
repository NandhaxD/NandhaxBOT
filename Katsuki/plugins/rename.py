
"""
Copyright © [2023-2024] @NandhaBots. All rights reserved. Reproduction, modification, distribution, or republication of this file without prior written permission from @NandhaBots is strictly prohibited. The Katsuki Telegram user bot has been developed with the Pyrogram library and utilizing Python programming language, making it a safe and secure option for users. Unauthorized use of this bot or any part of it may result in legal action. This project is owned by @Nandha, and any unauthorized use or distribution of this bot is strictly prohibited.
"""




import config
import os
from pyrogram import filters
from Katsuki import app, lang

THUMB_ID = "./IMG_20220701_185623_542.jpg"


@app.on_message(filters.command("rename",prefixes=config.HANDLER) & filters.me)
async def rename(_, message):
    try:
       filename = message.text.split(None,1)[1]
    except:
        return await message.edit("Ex: `.rename file.txt`")                                 
    msg = await message.edit(lang['download'])
    path = await message.reply_to_message.download(file_name=filename)
    await msg.edit_text(lang['upload'])
   
    await message.reply_document(document=path, thumb=THUMB_ID, quote=True)
    await msg.delete()
    os.remove(path)
    return 
    
    
    
