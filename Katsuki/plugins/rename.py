from Katsuki import app
from Katsuki.helpers.help_func import FileType
import config
import os
from pyrogram import filters

THUMB_ID = "./IMG_20220701_185623_542.jpg"




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
    
    
    
