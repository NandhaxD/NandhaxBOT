import config 


from pyrogram import filters
from Katsuki import app
from Katsuki.helpers.decorator import admin_only



@app.on_message(filters.command("ban", config.HANDLER) & filters.me)
@admin_only
async def ban(_, message):
   
   if len(message.text.split()) >= 2:
        user_id = message.from_user.id
   elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
   else:
       return await message.edit("WHO SHOULD I BAN?")
   try:
      IS_BAN = await app.ban_chat_member(
           chat_id=message.chat.id,
           user_id=user_id)
   except Exception as e:
         return await message.edit(f"[`ERROR`: `{e}`]")
   
  