from Katsuki import katsuki
from config import OWNER_ID, HANDLER
import os
from pyrogram import filters


async def FileType(message):
    if message.document:
          return message.document.mime_type.split("/")[1]
    elif message.photo:
          return message.photo.mime_type.split("/")[1]
    elif message.animation:
          return message.animation.mime_type.split("/")[1]
    elif message.video:
         return message.vedio.mime_type.split("/")[1]
    else:
         return False

@katsuki.on_message(filters.command("rename",prefixes=HANDLER) & filters.user(OWNER_ID))
async def rename(_, message):
    try:
       filename = message.text.split(None,1)[1]
    except:
        name = "Katsuki"
        try:
          if (await FileType(message=message.reply_to_message)) != False:
               filetype = await FileType(message=message.reply_to_message)
        except Exception as e:
               return await message.reply_text(f"Error: `{e}`")
        filename = "{name}.{filetype}".format(name=name, filetype=filetype)
    msg = await message.reply_text("⬇️ File has downloading...")
    path = await message.reply_to_message.download(file_name=filename)
    await msg.edit_text("⬆️ File has uplaoding")
    await message.reply_document(document=path)
    await msg.delete()
    os.remove(path)
    return 
    
    
    
