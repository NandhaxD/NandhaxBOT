from Katsuki import katsuki 
from pyrogram import filters 
from config import HANDLER, OWNER_ID


def get_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj


@katsuki.on_message(filters.command("id",prefixes=HANDLER) & filters.user(OWNER_ID))
async def id(_, m):
         reply = m.reply_to_message
         _id = ""
         if not reply:
               _id += f"**ʏᴏᴜʀ ɪᴅ**: `{m.from_user.id}`\n\n"
               _id += f"**ᴄʜᴀᴛ ɪᴅ**: `{m.chat.id}`\n\n"
               _id += f"**ᴍᴇssᴀɢᴇ ɪᴅ**: `{m.id}`\n\n"
               await reply.reply_text(text=(_id))
         if reply:
                 _id += f"**ʀᴇᴩʟɪᴇᴅ ᴜsᴇʀ ɪᴅ**:\n\n"
         file_info = get_id(message.reply_to_message)
         elif file_info:
                   _id += f"**{file_info.message_type}**:\n{file_info.file_id}"
         await m.reply_text(_id) 
                   
         
