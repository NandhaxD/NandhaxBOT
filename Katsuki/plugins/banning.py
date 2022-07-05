from pyrogram import Client, filters
from datetime import datetime, timedelta
from pyrogram.types import ChatPermissions, Message
from pyrogram.errors import UsernameInvalid, PeerIdInvalid, UserIdInvalid, ChatAdminRequired

from Katsuki import katsuki
from config import OWNER_ID, HANDLER

@katsuki.on_message(filters.command("ban24",prefixes=HANDLER) & filters.user(OWNER_ID))
async def member_ban(client: Client, message: Message):
    if message.chat.type in ["group", "supergroup"]:
        chat_id = message.chat.id
        me = await client.get_me
        notme = await message.chat.get_member(int(me.id))
        if not notme.can_restrict_members: # Checking wether the user have ban rights or not 
         await message.edit("**ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ʀɪɢʜᴛs ᴛᴏ ʙᴀɴ ᴛʜᴇ ᴜsᴇʀ **")
         return
        Ban = True
        if Ban:
            try:
                if message.reply_to_message:
                    user_id = message.reply_to_message.from_user.id
                else:
                    usr = await client.get_users(message.command[1])
                    user_id = usr.id
            except IndexError:
                await message.edit_text("ɪ ᴄᴀɴ'ᴛ ʙᴀɴ")
                return
            if user_id:
                try:
                    await katsuki.ban_chat_member(chat_id, user_id, datetime.now() + timedelta(days=1)) # Banning a member for 24 hours after that they can join the group back 🌚
                    await message.delete()
                except UsernameInvalid:
                    await message.edit_text("**ɪɴᴠᴀʟɪᴅ ᴜsᴇʀɴᴀᴍᴇ**")
                    return
                except PeerIdInvalid:
                    await message.edit_text("**ɪɴᴠᴀʟɪᴅ ᴜsᴇʀɴᴀᴍᴇ or userid**")
                    return
                except UserIdInvalid:
                    await message.edit_text("**ɪɴᴠᴀʟɪᴅ ᴜsᴇʀɪᴅ**")
                    return
                except ChatAdminRequired:
                    await message.edit_text("**ᴘᴇʀᴍɪssɪᴏɴ ᴅᴇɴɪᴇᴅ**")
                    return
                except Exception as e:
                    await message.edit_text(e)
                    return
        else:
            await message.edit_text("**ᴘᴇʀᴍɪssɪᴏɴ ᴅᴇɴɪᴇᴅ**")
            
