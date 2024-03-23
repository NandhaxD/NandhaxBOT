
"""
Copyright © [2023-2024] @NandhaBots. All rights reserved. Reproduction, modification, distribution, or republication of this file without prior written permission from @NandhaBots is strictly prohibited. The Katsuki Telegram user bot has been developed with the Pyrogram library and utilizing Python programming language, making it a safe and secure option for users. Unauthorized use of this bot or any part of it may result in legal action. This project is owned by @Nandha, and any unauthorized use or distribution of this bot is strictly prohibited.
"""



from pyrogram import enums
from pyrogram.types import Message 
from Katsuki import app


""" CHECK YOUR ACC HAS ADMIN IN CHAT """ 
  



async def is_admin(chat_id, user_id):
      kk = await app.get_chat_member(chat_id, user_id)
      admin = kk.status == enums.ChatMemberStatus.ADMINISTRATOR
      owner = kk.status == enums.ChatMemberStatus.OWNER
      if (admin or owner):
           return True, kk
      else:
           return False, kk
           

  
def admin_only(func): 
         async def wrapped(app:app, message:Message): 
             chat_id=message.chat.id 
             user_id=message.from_user.id 
             if message.chat.type==enums.ChatType.PRIVATE: 
                 return await message.edit("This command only work in groups.") 
             is_admin = await is_admin(chat_id, user_id)
             if not is_admin[0]:
                 return await message.edit("you're not admin.")
             return await func(app, message)                 
         return wrapped





def can_restrict_members(func): 
         async def wrapped(app:app, message:Message): 
             chat_id=message.chat.id 
             user_id=message.from_user.id 
             if message.chat.type==enums.ChatType.PRIVATE: 
                 return await message.edit("This command only work in gorups.") 
             is_admin = await is_admin(chat_id, user_id)
             if not is_admin[0]:  
                   return await message.edit("You're not admin.")
             elif not is_admin[1].privileges is None:
                    return await message.reply("I can't check admin rights here.")
             elif not is_admin[1].privileges.can_restrict_members:
                 return await message.edit("you can't ban users from here.")
             return await func(app, message)                 
         return wrapped 




        
