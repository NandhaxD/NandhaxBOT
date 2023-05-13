from telegraph import upload_file
from pyrogram import filters
from Katsuki import app
import config

@app.on_message(filters.command("tm", prefixes=config.HANDLER) & filters.me)
async def tm(_, message):
    await message.edit('processing...')
    reply_is = message.reply_to_message
    if not reply_is:
         return await message.edit_text("💔 Reply To The Media!")
    types = [True if reply_is.document else True if reply_is.photo else True if reply_is.animation else False][0]
    if types:
        path = await message.reply_to_message.download()
        grap = upload_file(path)
        for code in grap:
              url = "https://graph.org"+code
        return await message.edit(str(url))
        
