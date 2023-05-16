
"""
Copyright © [2023-2024] @NandhaBots. All rights reserved. Reproduction, modification, distribution, or republication of this file without prior written permission from @NandhaBots is strictly prohibited. The Katsuki Telegram user bot has been developed with the Pyrogram library and utilizing Python programming language, making it a safe and secure option for users. Unauthorized use of this bot or any part of it may result in legal action. This project is owned by @Nandha, and any unauthorized use or distribution of this bot is strictly prohibited.
"""




import config 


from pyrogram import filters
from Katsuki import app
from Katsuki.helpers.decorator import admin_only



@app.on_message(filters.command("ban", config.HANDLER) & filters.me)
@admin_only
async def ban_chat_member(app, message):
   
   if len(message.text.split()) >= 2:
        user_id = message.from_user.id
   elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
   else:
       return await message.edit("[`WHO SHOULD I BAN?`]")
   try:
      await app.ban_chat_member(
           chat_id=message.chat.id,
           user_id=user_id)
   except Exception as e:
         return await message.edit(f"[`ERROR`: `{e}`]")
   return await message.edit("[`BANNED`]")
   
  