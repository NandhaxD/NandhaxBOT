from config import OWNER_ID, HANDLER
from Katsuki import katsuki
from Katsuki.utils import section
from pyrogram import filters 

@katsuki.on_message(filters.command("cinfo",prefixes=HANDLER) & filters.user(OWNER_ID))
async def cinfo(_, m):
       reply = m.reply_to_message
       if not reply:
            await m.reply_text("yoo! ultra noob reply to channel")
            return 
       if not reply.sender_chat:
            await m.reply_text("yoo! ultra noob reply to channel")
            return 
       if reply.sender_chat:
             message = await m.reply_text("information gathering!!!")
             id = reply.sender_chat.id
             type = reply.sender_chat.type
             name = reply.sender_chat.title
             username = reply.sender_chat.username
             pfp = reply.sender_chat.photo
       if not pfp:
            text = f"✪ **TYPE:** Channel\n\n"
            text += f"✪ **ID:** {id}\n\n"
            text += f"✪ **NAME:** {name}\n\n"
            text += f"✪ **USERNAME:** @{username}\n\n"
            text += f"✪ **MENTION:** [link](t.me/{username})"
            await m.reply_text(text)
            await message.delete()
            return 
       image = reply.sender_chat.photo
       if image:
            photo = await katsuki.download_media(image.big_file_id)
            text = f"✪ **TYPE:** Channel\n\n"
            text += f"✪ **ID:** {id}\n\n"
            text += f"✪ **NAME:** {name}\n\n"
            text += f"✪ **USERNAME:** @{username}\n\n"
            text += f"✪ **MENTION:** [link](t.me/{username})"
            await katsuki.send_photo(m.chat.id,photo,caption=(text))
            await message.delete()
              
no_reply_user = """ ╒═══「 Appraisal results:\n 」
**ɪᴅ**: `{}`
**ᴅᴄ**: `{}`
**ғɪʀsᴛ ɴᴀᴍᴇ**: `{}`
**ᴜsᴇʀɴᴀᴍᴇ**: `{}`
**ᴘᴇʀᴍᴀʟɪɴᴋ**: `{}`
**ᴜsᴇʀʙɪᴏ**: `{}`
"""

              
@katsuki.on_message(filters.command("info",prefixes=HANDLER) & filters.user(OWNER_ID))
async def info(_, m):
            reply = m.reply_to_message
            user = reply.from_user or m.from_user
            info = await app.get_chat(user.id)
            user_bio = info.bio
            user_link = f"[link](tg://user?id=user.id)"
            await m.reply_photo(no_reply_user.format(user.id,
            user.dc_id, user.first_name, user.username, user_link, user_bio))
                


