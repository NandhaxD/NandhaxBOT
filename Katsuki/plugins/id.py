from Katsuki import katsuki 
from pyrogram import filters 
from config import HANDLER, OWNER_ID


@katsuki.on_message(filters.command("id",prefixes=HANDLER) & filters.user(OWNER_ID))
async def id(_, m):
         reply = m.reply_to_message
         if not reply:
               text = f"**ʏᴏᴜʀ ɪᴅ**: `{m.from_user.id}`\n\n"
               text += f"**ᴄʜᴀᴛ ɪᴅ**: `{m.chat.id}`\n\n"
               text += f"**ᴍᴇssᴀɢᴇ ɪᴅ**: `{m.id}`"
               await m.reply_text(text=(text)) 
          if not reply.sticker or reply.animation:
               text = f"**ʏᴏᴜʀ ɪᴅ**: `{m.from_user.id}`\n\n"
               text += f"**ʀᴇᴘʟɪᴇᴅ ɪᴅ**: `{reply.from_user.id}`\n\n"
               text += f"**ᴄʜᴀᴛ ɪᴅ**: `{m.chat.id}`\n\n"
               text += f"**ᴍᴇssᴀɢᴇ ɪᴅ**: `{m.id}`"
               await m.reply_text(text=(text))
               return 
           elif reply.sticker:
                  text = f"**ʏᴏᴜʀ ɪᴅ**: `{m.from_user.id}`\n\n"
                  text += f"**ʀᴇᴘʟɪᴇᴅ ɪᴅ**: `{reply.from_user.id}`\n\n"
                  text += f"**ᴄʜᴀᴛ ɪᴅ**: `{m.chat.id}`\n\n"
                  text += f"**ᴍᴇssᴀɢᴇ ɪᴅ**: `{m.id}`\n\n\n"
                  text += f"**sᴛɪᴄᴋᴇʀ ɪᴅ**: `{reply.sticker.file_id}`"
                  await m.reply_text(text=(text)) 
                  return 
           elif reply.animation:
               text = f"**ʏᴏᴜʀ ɪᴅ**: `{m.from_user.id}`\n\n"
               text += f"**ʀᴇᴘʟɪᴇᴅ ɪᴅ**: `{reply.from_user.id}`\n\n"
               text += f"**ᴄʜᴀᴛ ɪᴅ**: `{m.chat.id}`\n\n"
               text += f"**ᴍᴇssᴀɢᴇ ɪᴅ**: `{m.id}`\n\n\n"
               text += f"**ɢɪғ ɪᴅ**: `{reply.animation.file_id}`"
               await m.reply_text(text=(text)) 
