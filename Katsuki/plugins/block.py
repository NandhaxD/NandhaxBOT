from Katsuki import katsuki 
from pyrogram import filters 
from config import HANDLER, OWNER_ID

@katsuki.on_message(filters.command("block",prefixes=HANDLER) & filters.user(OWNER_ID))
async def id(_, m):
         reply = m.reply_to_message
         if not reply: 
               await m.reply_text("Wʜᴏᴍ sʜᴏᴜʟᴅ ɪ ʙʟᴏᴄᴋ ᴋɪᴅᴅᴏ") 
         if reply:
            await reply.reply_text(f'Bʟᴏᴄᴋᴇᴅ ᴛʜɪs ɴɪɢɢᴀ {reply.from_user.first_name}')
            await app.block_user(reply.from_user.id)
            await m.delete()
            
            
@katsuki.on_message(filters.command("unblock",prefixes=HANDLER) & filters.user(OWNER_ID))
async def id(_, m):
         reply = m.reply_to_message
         if not reply: 
               await m.reply_text("Wʜᴏᴍ sʜᴏᴜʟᴅ ɪ ʙʟᴏᴄᴋ ᴋɪᴅᴅᴏ") 
         if reply:
            await reply.reply_text(f'Uɴʙʟᴏᴄᴋᴇᴅ ᴛʜɪs ɴɪɢɢᴀ {reply.from_user.first_name}')
            await app.unblock_user(reply.from_user.id)
            await m.delete()
