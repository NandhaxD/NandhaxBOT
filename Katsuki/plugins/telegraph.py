from telegraph import upload_file
from pyrogram import filters
from Katsuki import katsuki
from config import HANDLER,  OWNER_ID

@katsuki.on_message(filters.command("tm", prefixes=HANDLER) & filters.user(OWNER_ID))
async def tm(_, message):
    m = await message.reply_text("UwU processing...")
    try:
     reply_is = message.reply_to_message
    except:
        await m.edit("💔 Reply To The Media!")
    types = [True if reply_is.document else True if reply_is.photo else True if reply_is.animation else False][0]
    if types:
        path = await message.reply_to_message.download()
        uWu = upload_file(path)
        for code in uWu:
              url = "https://graph.org/file/"+code
        await m.edit(str(url))
        
