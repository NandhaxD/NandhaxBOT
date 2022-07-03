import random 
from config import HANDLER, OWNER_ID, KATSUKI
from pyrogram import filters 
from Katsuki import katsuki

@katsuki.on_message(filters.command("alive",prefixes=HANDLER) & filters.user(OWNER_ID))
async def alive(_, m):
      await m.reply_photo(random.choice(KATSUKI))
