
"""
Copyright © [2023-2024] @NandhaBots. All rights reserved. Reproduction, modification, distribution, or republication of this file without prior written permission from @NandhaBots is strictly prohibited. The Katsuki Telegram user bot has been developed with the Pyrogram library and utilizing Python programming language, making it a safe and secure option for users. Unauthorized use of this bot or any part of it may result in legal action. This project is owned by @Nandha, and any unauthorized use or distribution of this bot is strictly prohibited.
"""

import config
from pyrogram import enums, filters
from pyrogram.types import Message 
from nandha import lang , bot, app
from nandha.database.devs import get_users


class String:
    def not_admin(who):
        text = f"{who} don't have admin rights."
        return text
    def not_premission(who, premission):
        text = f"{who} don't have the {premission} "
        return text
         
      

""" CHECK YOUR ACC HAS ADMIN IN CHAT """

async def admin_check(client, chat_id, user_id):
      userinfo = await client.get_chat_member(chat_id, user_id)
      if userinfo.status in (enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER):
           return True, userinfo
      else:
           return False, userinfo
           
    
def devs_only(func):
     async def wrapped(client, message):
          user_id = message.from_user.id
          list = await get_users()
          if (user_id != int(config.OWNER_ID) and (not user_id in list)):
                return 
          return await func(client, message)
     return wrapped


def admin_only(client):
     def decorator(func):
         async def wrapped(_, message):
             chat_id = message.chat.id
             user_id = message.from_user.id
             client_info = await client.get_me()
             if client_info.is_bot:
                  bot_admin , bot_obj = await admin_check(bot, chat_id, config.BOT_ID)
                  if not bot_admin:
                      return await message.reply_text(
                         text=String.not_admin(who='I'))
                      
             admin, admin_obj = await admin_check(client, chat_id, user_id)
             if admin:
                 return await func(_, message)
             else:
                 return await message.reply_text(
                     text=String.not_admin(who='You')
                 )
         return wrapped
     return decorator


def admin_rights(client, premission):
       def decorator(func):
             async def wrapped(_, message):
                  chat_id = message.chat.id
                  user_id = message.from_user.id
                  client_info = await client.get_me()
                 
                  if client_info.is_bot:
                      bot_admin , bot_obj = await admin_check(bot, chat_id, client_info.id)
                      if not bot_admin:
                          return await message.reply_text(
                             text=String.not_admin(who='I'))
                      elif bot_obj.privileges:
                           privileges_dict = bot_obj.privileges.__dict__
                           if not privileges_dict.get(premission):
                                return await message.reply(
                                    text=String.not_premission(who='I', premission=premission)
                                 
                  admin, admin_obj = await admin_check(client, chat_id, user_id)
                  if admin and admin_obj.privileges:
                      privileges_dict = admin_obj.privileges.__dict__
                      if privileges_dict.get(premission):
                            await func(_, message)
                      else:
                          return await message.reply(f'`You are missing the [{premission}] required premission.`')
                  else:
                      return await message.reply('You are not admin.')
             return wrapped
       return decorator



@bot.on_message(filters.command('del'))
@admin_rights(bot, 'can_delete_messages')
async def delete(_, message):
       return await message.reply('Yes i have the delete premission')
          

        


        
