
import config
from pyrogram import filters
from Katsuki import katsuki


@katsuki.on_message(filters.command("ban", prefixes=config.HANDLER) & filters.user(config.OWNER_ID))
async def ban_member(_, message):
    
    if message.reply_to_message:
         user_id = message.reply_to_message.from_user.id  
    else:
      try:
         user_id = message.text.split()[1]
      except:
          return await message.edit("Provide USER_ID To Ban!")
    try:
       owo = await message.chat.ban_member(user_id)
    except Exception as e:
        return await message.edit(f"Somthing wrong Happens:\n{e}")
    name = (await katsuki.get_users(user_id)).first_name
    return await message.edit(f"{name} has been banned!")


@katsuki.on_message(filters.command("unban") & filters.user(config.OWNER_ID))
async def unban_member(_, message):
    
    if message.reply_to_message:
         user_id = message.reply_to_message.from_user.id  
    else:
      try:
         user_id = message.text.split()[1]
      except:
          return await message.edit("Provide USER_ID To UnBan!")
    try:
       owo = await message.chat.unban_member(user_id)
    except Exception as e:
        return await message.edit(f"Somthing wrong Happens:\n{e}")
    name = (await katsuki.get_users(user_id)).first_name
    return await message.edit(f"{name} Has Been UnBanned!")

