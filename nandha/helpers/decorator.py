
"""
Copyright © [2023-2024] @NandhaBots. All rights reserved. Reproduction, modification, distribution, or republication of this file without prior written permission from @NandhaBots is strictly prohibited. The Katsuki Telegram user bot has been developed with the Pyrogram library and utilizing Python programming language, making it a safe and secure option for users. Unauthorized use of this bot or any part of it may result in legal action. This project is owned by @Nandha, and any unauthorized use or distribution of this bot is strictly prohibited.
"""

import config
from pyrogram import enums, filters
from pyrogram.types import Message 
from nandha import lang, bot
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
      results = []
      userinfo = await client.get_chat_member(chat_id, user_id)
      admin = userinfo.status == enums.ChatMemberStatus.ADMINISTRATOR
      owner = userinfo.status == enums.ChatMemberStatus.OWNER
      if (admin or owner):
           results.append(True)
           results.append(userinfo)
           return
      else:
           results.append(False)
           results.append(False)
           return
           

def admin_only(func): 
         async def wrapped(client, message): 
             chat_id=message.chat.id 
             user_id=message.from_user.id 

             if message.chat.type == enums.ChatType.PRIVATE:
                  return await func(client, message)
                 
             is_admin = await admin_check(client, chat_id, user_id)
             if not is_admin[0]:
                 return await message.edit(
                   String.not_admin()
                 )
             else:
                 return await func(client, message)                 
         return wrapped



def can_delete_messages(client, message):
     async def decorator(func):
         async def wrapped(*args, **kwargs):
              chat_id = message.chat.id 
              user_id = message.from_user.id 

              if message.chat.type == enums.ChatType.PRIVATE:
                  return await func(*args, **kwargs)
              
              nandha = await admin_check(client, chat_id, user_id)
              if not nandha[0]:
                    return await message.edit(String.not_admin())
              else:
                 if nandha[1].privileges.can_delete_messages:
                    return await func(*args, **kwargs)
                 else:
                    return await message.edit(String.not_delete_per())
         return wrapped                 
     return decorator      



@bot.on_message(filters.command('candel'))
@can_delete_messages(client=bot, message=Message)
async def candel(_, message):
      return await message.reply('yes i can delete')
      
    
def devs_only(func):
     async def wrapped(client, message: Message):
          user_id = message.from_user.id
          list = await get_users()
          if (user_id != int(config.OWNER_ID) and (not user_id in list)):
                return 
          return await func(client, message)
     return wrapped 
  


def can_restrict_members(func):
     async def wrapped(client, message: Message):
          chat_id=message.chat.id 
          user_id=message.from_user.id 

          if message.chat.type == enums.ChatType.PRIVATE:
              return await func(client, message)
              
          nandha = await admin_check(client, chat_id, user_id)
          if not nandha[0]:
               return await message.edit(String.not_admin())
          else:
             if nandha[1].privileges.can_restrict_members:
                 return await func(client, message)
             else:
                 return await message.edit(String.not_restrict_per())
     return wrapped





        
