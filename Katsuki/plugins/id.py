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
               no_reply += f"**ᴍsɢ ɪᴅ**: `{m.id}`"
               await reply.reply_text(text=(no_reply)) 
         if reply.from_user:
               _reply += f"**ʏᴏᴜʀ ɪᴅ**: `{m.from_user.id}`\n\n"
               _reply += f"**ʀᴇᴘʟɪᴇᴅ ɪᴅ**: `{reply.from_user.id}`\n\n"
               _reply += f"**ᴄʜᴀᴛ ɪᴅ**: `{m.chat.id}`\n\n"
               _reply += f"**ʀᴇᴘʟɪᴇᴅ ᴍsɢ ɪᴅ**: `{reply.id}`\n\n"
         if reply.sender_chat:
                _reply += f"\n\n**ᴄʜᴀɴɴᴇʟ  ɪᴅ**: `{reply.sender_chat.id}`\n\n"
         if reply.sticker:
                _reply += f"**sᴛɪᴄᴋᴇʀ ɪᴅ**: `{reply.sticker.file_id}`"
         elif reply.animation:
                _reply += f"**ᴀɴɪᴍᴀᴛɪᴏɴ ɪᴅ**: `{reply.animation.file_id}`"
         elif reply.document:
                _reply += f"**ᴅᴏᴄᴜᴍᴇɴᴛ ɪᴅ**: `{reply.document.file_id}`"
         elif reply.photo:
                _reply += f"**ᴘʜᴏᴛᴏ ɪᴅ**: `{reply.photo.file_id}`"
         await reply.reply_text(_reply)
         await m.delete()
                   

         



#test
