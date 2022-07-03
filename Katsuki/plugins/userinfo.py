from config import OWNER_ID, HANDLER
from Katsuki import katsuki
from Katsuki.utils import section
from pyrogram import filters 
from pyrogram.raw import functions
from pyrogram.errors import PeerIdInvalid

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
              
no_reply_user = """ ╒═══「 Appraisal results:」
**ɪᴅ**: `{}`
**ᴅᴄ**: `{}`
**ғɪʀsᴛ ɴᴀᴍᴇ**: {}
**ᴜsᴇʀɴᴀᴍᴇ**: @{}
**ᴘᴇʀᴍᴀʟɪɴᴋ**: {}
**ᴜsᴇʀʙɪᴏ**: {}

**ᴄᴏᴍᴍᴏɴ ᴄʜᴀᴛs:** {}
"""

async def commons(bot: katsuki, get_user):
    common = await bot.send(
        functions.messages.commonsChats(
            user_id=await bot.resolve_peer(get_user), max_id=0, limit=0
        )
    )
    return common
              
@katsuki.on_message(filters.command("info",prefixes=HANDLER) & filters.user(OWNER_ID))
async def info(_, m):
            reply = m.reply_to_message
            if len(m.command) < 2:
                  await m.reply_text("ɢɪᴠᴇ ᴍᴇ ɪᴅ")
                  return 
            id_user = m.text.split(" ")[1]
            msg =  await m.reply_text("ɪɴғᴏʀᴍᴀᴛɪᴏɴ ɢᴀᴛʜᴇʀɪɴɢ!")
            info = await katsuki.get_chat(id_user)
            common = await commons(bot, id_user)
            if info.photo:
                   file_id = info.photo.big_file_id
                   photo = await katsuki.download_media(file_id)
                   user_id = info.id
                   first_name = info.first_name
                   username = info.username 
                   user_bio = info.bio
                   dc_id = info.dc_id
                   user_link = f"[link](tg://user?id={user_id})"
                   await katsuki.send_photo(m.chat.id,photo,caption=no_reply_user.format(user_id,
                       dc_id, first_name, username, user_link, user_bio, common))
            elif not info.photo:
                   user_id = info.id
                   first_name = info.first_name
                   username = info.username 
                   user_bio = info.bio
                   dc_id = info.dc_id
                   user_link = f"[link](tg://user?id={user_id})"
                   await m.reply_text(text=no_reply_user.format(user_id,
                      dc_id, first_name, username, user_link, user_bio, common))
            await msg.delete()


