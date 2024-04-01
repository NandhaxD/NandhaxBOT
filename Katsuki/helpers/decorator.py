
"""
Copyright © [2023-2024] @NandhaBots. All rights reserved. Reproduction, modification, distribution, or republication of this file without prior written permission from @NandhaBots is strictly prohibited. The Katsuki Telegram user bot has been developed with the Pyrogram library and utilizing Python programming language, making it a safe and secure option for users. Unauthorized use of this bot or any part of it may result in legal action. This project is owned by @Nandha, and any unauthorized use or distribution of this bot is strictly prohibited.
"""

import config

from pyrogram import enums
from pyrogram.types import Message 
from Katsuki import app, lang
from Katsuki.database.devs import get_users


""" CHECK YOUR ACC HAS ADMIN IN CHAT """ 
  



async def admin_check(chat_id, user_id):
      kk = await app.get_chat_member(chat_id, user_id)
      admin = kk.status == enums.ChatMemberStatus.ADMINISTRATOR
      owner = kk.status == enums.ChatMemberStatus.OWNER
      if (admin or owner):
           return True, kk
      else:
           return False, kk
           



def can_delete_messages(func):
     async def wrapped(app: app, message: Message):
          user_id = message.from_user.id
          chat_id = message.chat.id
          if message.chat.type==enums.ChatType.PRIVATE:
               return await func(app, message)
          else:
               nandha = await admin_check(chat_id, user_id)
               if nandha[0] == True:
                    if nandha[1].privileges.can_delete_messages:
                            return await func(app, message)
                    else:
                         return await message.edit(lang['delete_01'])
               else:
                    return await message.edit(lang['not_admin'])
     return wrapped                 
              
      

def devs_only(func):
     async def wrapped(app: app, message: Message):
          user_id = message.from_user.id
          list = await get_users()
          if (user_id != int(config.OWNER_ID) and (not user_id in list)):
                return 
          return await func(app, message)
     return wrapped 
  

def admin_only(func): 
         async def wrapped(app: app, message:Message): 
             chat_id=message.chat.id 
             user_id=message.from_user.id 
             if message.chat.type==enums.ChatType.PRIVATE: 
                 return await message.edit(lang['only_group']) 
             is_admin = await admin_check(chat_id, user_id)
             if not is_admin[0]:
                 return await message.edit(lang['not_admin'])
             return await func(app, message)                 
         return wrapped


def can_restrict_members(func): 
         async def wrapped(app: app, message:Message): 
             chat_id=message.chat.id 
             user_id=message.from_user.id 
             if message.chat.type==enums.ChatType.PRIVATE: 
                 return await message.edit(lang['only_group']) 
             is_admin = await admin_check(chat_id, user_id)
             if not is_admin[0]:  
                   return await message.edit(lang['not_admin'])
             elif is_admin[1].privileges is None:
                    return await message.edit(lang['not_check_admin'])
             elif not is_admin[1].privileges.can_restrict_members:
                 return await message.edit(lang['ban_04'])
             return await func(app, message)                 
         return wrapped 




        
