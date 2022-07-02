from config import HANDLER
from pyrogram import filters 
from Katsuki import katsuki

@katsuki.on_message(filters.command("alive",prefixes=HANDLER) & filters.user(config.USER))
async def alive(_, m):
      await m.reply_text("Hey sir I'm alive")
