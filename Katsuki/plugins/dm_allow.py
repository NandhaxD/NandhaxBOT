
import config

from pyrogram import filters
from Katsuki import katsuki
from Katsuki.katuski_db.dm_allow import (
allowed_to_dm, disallowed_to_dm, get_allowed_users )





@katsuki.on_message(filters.command("allow", config.HANDLER) & filters.user(config.OWNER_ID))
async def allow_users_dm(_, message):
     if message.reply_to_message:
           user_id = message.reply_to_message.from_user.id
     else:
         return await message.edit("=> No Reply?")
     allowed_users = await get_allowed_users()
     if user_id not in allowed_users:
            await allowed_to_dm(user_id)
            return await message.edit("Allowed To Access Dm!")
     else:
         return await message.edit("=> Already Allowed To Dm!")
  
@katsuki.on_message(filters.command("disallow", config.HANDLER) & filters.user(config.OWNER_ID))
async def disallow_users_dm(_, message):
     if message.reply_to_message:
           user_id = message.reply_to_message.from_user.id
     else:
         return await message.edit("=> No Reply?")
     allowed_users = await get_allowed_users()
     if user_id in allowed_users:
            await disallowed_to_dm(user_id)
            return await message.edit("Disallowed To Access Dm!")
     else:
         return await message.edit("=> Already (: Disallowed To Dm!")



  
