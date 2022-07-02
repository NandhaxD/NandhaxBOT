from config import HANDLER, OWNER_ID
from pyrogram import filters 
from Katsuki import katsuki

@katsuki.on_message(filters.command("alive",prefixes=HANDLER) & filters.user(OWNER_ID))
async def alive(_, m):
      await m.reply_text("Hey sir I'm alive")
