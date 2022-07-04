from Katsuki import katsuki
from pyrogram import filters
from config import ( OWNER_ID, HANDLER) 

@katsuki.on_message(filters.command("join",prefixes=HANDLER) & filters.user(OWNER_ID))
async def joinchat(_, m)
          link =  m.text.split(" ")[1]
          katsuki.join_chat(link)
          await m.reply_text(f"Successfully joined {link}")
