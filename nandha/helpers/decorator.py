
"""
Copyright © [2023-2024] @NandhaBots. All rights reserved. Reproduction, modification, distribution, or republication of this file without prior written permission from @NandhaBots is strictly prohibited. The Katsuki Telegram user bot has been developed with the Pyrogram library and utilizing Python programming language, making it a safe and secure option for users. Unauthorized use of this bot or any part of it may result in legal action. This project is owned by @Nandha, and any unauthorized use or distribution of this bot is strictly prohibited.
"""

import config
from pyrogram import enums, filters
from pyrogram.types import Message 
from nandha import lang , bot, app
from nandha.database.devs import get_users


class String:
    def not_admin():
        text = "You're not admin."
        return text
    def not_delete_per():
         text = "You don't have delete permission."
         return text
    def not_restrict_per():
        text = "You don't have rights to restrict members here."
        return text
         
      

""" CHECK YOUR ACC HAS ADMIN IN CHAT """

async def admin_check(client, chat_id, user_id):
      userinfo = await client.get_chat_member(chat_id, user_id)
      if userinfo.status in (enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER):
           return True, userinfo
      else:
           return False, userinfo
           

def admin_only(func): 
         async def wrapped(client, message): 
             chat_id = message.chat.id 
             user_id = message.from_user.id 

             if message.chat.type == enums.ChatType.PRIVATE:
                  return await func(client, message)
                 
             admin, admin_obj = await admin_check(client, chat_id, user_id)
             if not admin:
                 return message.edit(
                   String.not_admin()
                 )
             else:
                 return await func(client, message)                 
         return wrapped


def can_delete_messages(func):
         async def wrapped(client, message):
              chat_id = message.chat.id 
              user_id = message.from_user.id 

              if message.chat.type == enums.ChatType.PRIVATE:
                  return await func(client, message)
              
              admin, admin_obj = await admin_check(client, chat_id, user_id)
              if not admin:
                    return await message.edit(
                        String.not_admin()
                    )
              else:
                 if admin_obj.privileges.can_delete_messages:
                    return await func(client, message)
                 else:
                    return await message.edit(String.not_delete_per())
         return wrapped   


    
def devs_only(func):
     async def wrapped(client, message):
          user_id = message.from_user.id
          list = await get_users()
          if (user_id != int(config.OWNER_ID) and (not user_id in list)):
                return 
          return await func(client, message)
     return wrapped 
  


def can_restrict_members(func):
     async def wrapped(client, message):
          chat_id=message.chat.id 
          user_id=message.from_user.id 

          if message.chat.type == enums.ChatType.PRIVATE:
              return await func(client, message)
              
          admin, admin_obj = await admin_check(client, chat_id, user_id)
          if not admin:
               return await message.edit(String.not_admin())
          else:
             if admin_obj.privileges.can_restrict_members:
                 return await func(client, message)
             else:
                 return await message.edit(String.not_restrict_per())
     return wrapped



def can_fuck(client):
     def decorator(func):
          async def wrapped(_, message):
               chat_id = message.chat.id
               user_id = 6384531312
               admin, admin_obj = await admin_check(client, chat_id, user_id)
               if admin:
                    return await func(_, message)
               else:
                    return await message.reply('no?')
          return wrapped
     return decorator



@bot.on_message(filters.command('admin'))
@can_fuck(bot)
async def admin(_, message):
      return await message.reply('whst')
                   
                   
                 
          

        


        
