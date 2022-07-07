import config 
import requests 
from Katsuki import katsuki
from pyrogram import filters 


@katsuki.on_message(filters.command("logo",prefixes=config.HANDLER) &  filters.user(config.OWNER_ID))
async def logomaker(_, m):
             if len(m.command) < 2:
                     await m.reply_text("ɢɪᴠᴇ ᴍᴇ ᴀ ᴛᴇxᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ʟᴏɢᴏ")
             text = m.text.split(None, 1)[1]
             msg = await m.reply_text("ʏᴏᴜʀ ʟᴏɢᴏ ᴀs ɢᴇɴᴇʀᴀᴛɪɴɢ")
             image = requests.get((f"https://single-developers.up.railway.app/logohq?name={text}").replace(" ","%20")).history[1].url
             if image:
                 await m.reply_photo(image)
             await msg.delete()
