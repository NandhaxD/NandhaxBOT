from Katsuki import katsuki 
from pyrogram import filters 
from config import HANDLER, OWNER_ID




@katsuki.on_message(filters.command("id",prefixes=HANDLER) & filters.user(OWNER_ID))
async def id(_, m):
         reply = m.reply_to_message
         _reply = ""
         if not reply:
               no_reply = f"**ʏᴏᴜʀ ɪᴅ**: `{m.from_user.id}`\n\n"
               no_reply += f"**ᴄʜᴀᴛ ɪᴅ**: `{m.chat.id}`\n\n"
               no_reply += f"**ᴍᴇssᴀɢᴇ ɪᴅ**: `{m.id}`"
               await m.reply_text(text=(no_reply)) 
         if reply:
               _reply += f"**ʏᴏᴜʀ ɪᴅ**: `{m.from_user.id}`\n\n"
               _reply += f"**ʀᴇᴘʟɪᴇᴅ ɪᴅ**: `{reply.from_user.id}`\n\n"
               _reply += f"**ᴄʜᴀᴛ ɪᴅ**: `{m.chat.id}`\n\n"
               _reply += f"**ᴍᴇssᴀɢᴇ ɪᴅ**: `{m.id}`"
         elif reply.sticker:
                _reply += f"**sᴛɪᴄᴋᴇʀ ɪᴅ**: `{reply.sticker.file_id}`"
         await m.reply_text(_reply)
                   

         



#test
