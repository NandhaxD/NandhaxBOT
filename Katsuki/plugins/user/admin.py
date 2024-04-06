
"""
Copyright © [2023-2024] @NandhaBots. All rights reserved. Reproduction, modification, distribution, or republication of this file without prior written permission from @NandhaBots is strictly prohibited. The Katsuki Telegram user bot has been developed with the Pyrogram library and utilizing Python programming language, making it a safe and secure option for users. Unauthorized use of this bot or any part of it may result in legal action. This project is owned by @Nandha, and any unauthorized use or distribution of this bot is strictly prohibited.
"""




import config, asyncio

from pyrogram import filters, enums
from Katsuki import app, bot, lang
from Katsuki.helpers.decorator import admin_only, can_restrict_members, can_delete_messages


@app.on_message(filters.me & filters.command(['admins', 'adminlist'], prefixes=config.HANDLER))
@admin_only
async for def adminlist(_, message):
       
       chat_name = message.chat.title
       admin_str = f"Admin from {chat_name}:\n"
       if not len(message.text.split()) < 2:
           try:
               chat_id = message.text.split(None, 1)[1]
               async for m in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTATORS):
                       admin_str += f"➤ {m.user.mention}\n"
               await message.edit(admin_str)
           except Exception as e:
                  return await message.edit(lang['error'].format(e))
       else:
           try:
               chat_id = message.chat.id
               async for m in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTATORS):
                     admin_str += f"➤ {m.user.mention}\n"
               await message.edit(admin_str)
           except Exception as e:
                  return await message.edit(lang['error'].format(e))
                  


@app.on_message(filters.me & filters.command(['purge', 'del'], prefixes=config.HANDLER))
@can_delete_messages
async def purge_messages(_, message):
       chat_id = message.chat.id
       reply = message.reply_to_message
       if reply:
             if message.text.split()[0][1:0].lower() == 'del':
                   try:
                       await reply.delete()
                       return await message.delete()
                   except:
                       pass
             else:
                reply_id = message.reply_to_message.id
                message_id = message.id
                msg_ids = []
                for msg in range(reply_id, message_id):
                    msg_ids.append(msg)
                await app.delete_messages(chat_id, msg_ids)
                await message.edit(lang['success'])
                await asyncio.sleep(3)
                await message.delete()
                
       else:
            return await message.edit(lang['reply_to'])
            
             
@app.on_message(filters.me & filters.command('unbanall', config.HANDLER))
@can_restrict_members
async def unban_all_members(_, message):
     chat_id = message.chat.id
     chat_name = message.chat.title

     users = []
     success = 0
     msg = await message.edit('~ Searching For Unban Members.')
     async for m in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.BANNED):
        try:
              users.append(m.user.id)
              await app.unban_chat_member(chat_id, m.user.id)
              success += 1
        except:
              pass
     await bot.send_message(
            chat_id=config.OWNER_ID,
            text=lang['unbanall_01'].format(len(users), chat_name, success))
       
     await msg.edit(lang['unbanall_02'].format(len(users), chat_name, success))

            

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
   await bot.send_message(chat_id=config.OWNER_ID, text=lang['ban_03'].format(success, failures, chat_name))
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
   
  
