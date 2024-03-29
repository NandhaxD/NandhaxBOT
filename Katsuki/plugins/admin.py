
"""
Copyright © [2023-2024] @NandhaBots. All rights reserved. Reproduction, modification, distribution, or republication of this file without prior written permission from @NandhaBots is strictly prohibited. The Katsuki Telegram user bot has been developed with the Pyrogram library and utilizing Python programming language, making it a safe and secure option for users. Unauthorized use of this bot or any part of it may result in legal action. This project is owned by @Nandha, and any unauthorized use or distribution of this bot is strictly prohibited.
"""




import config, asyncio

from pyrogram import filters, enums
from Katsuki import app, bot, lang
from Katsuki.helpers.decorator import admin_only, can_restrict_members



@app.on_message(filters.me & filters.command("banall", config.HANDLER))
@can_restrict_members
async def ban_all_members(_, message):
   chat_id = message.chat.id
   chat_name = message.chat.title
   
   success = 0
   failures = 0

   async for m in app.get_chat_members(chat_id=chat_id):
          
    try:         
          service = await app.ban_chat_member(chat_id=chat_id, user_id=m.user.id)             
          if service:
              await service.delete()
              success += 1           
          await asyncio.sleep(3)
          await message.edit(lang['ban_03'].format(success, failures, chat_name))          
    except:
         failures += 1   
   await bot.send_message(chat_id=config.OWNER_ID, text=lang['ban_03'].format(success=success, failures=failures, chat_name))
   await message.edit(lang['ban_03'].format(success, failures, chat_name))


@app.on_message(filters.command("ban", config.HANDLER) & filters.me)
@can_restrict_members
async def ban_chat_member(app, message):
        
   if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        mention = message.reply_to_message.from_user.mention
   else:
       return await message.edit(lang['ban_01'])
   try:
      await app.ban_chat_member(
           chat_id=message.chat.id,
           user_id=user_id)
   except Exception as e:
         return await message.edit(lang['error'].format(e))
   return await message.edit(lang['ban_02'].format(mention))
   
  
