import config
from pyrogram import filters 
from Katsuki import Katsuki

@Katsuki.on_message(filters.command("alive",prefixes=config.HANDLER) & filters.user(config.USER))
async def alive(_, m):
      await m.reply_text("Hey sir I'm alive")
