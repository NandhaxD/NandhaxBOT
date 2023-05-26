
"""
Copyright © [2023-2024] @NandhaBots. All rights reserved. Reproduction, modification, distribution, or republication of this file without prior written permission from @NandhaBots is strictly prohibited. The Katsuki Telegram user bot has been developed with the Pyrogram library and utilizing Python programming language, making it a safe and secure option for users. Unauthorized use of this bot or any part of it may result in legal action. This project is owned by @Nandha, and any unauthorized use or distribution of this bot is strictly prohibited.
"""



from pyrogram import enums
from pyrogram.types import Message 
from Katsuki import app


""" CHECK YOUR ACC HAS ADMIN IN CHAT """ 
  

def admin_only(func): 
         async def wrapped(app:app, message:Message): 
             chat_id=message.chat.id 
             user_id=message.from_user.id 
             if message.chat.type==enums.ChatType.PRIVATE: 
                 return await message.edit("[`THIS COMMAND ONLY FOR GROUP`]") 
             check=await message.chat.get_member(user_id) 
             is_admin = check.status==enums.ChatMemberStatus.ADMINISTRATOR 
             is_owner = check.status==enums.ChatMemberStatud.OWNER
             if not (is_admin and is_owner): 
                 return await message.edit("[`YOU ARE NOT ADMIN`]")
             return await func(app, message)                 
         return wrapped





def can_restrict_members(func): 
         async def wrapped(app:app, message:Message): 
             chat_id=message.chat.id 
             user_id=message.from_user.id 
             if message.chat.type==enums.ChatType.PRIVATE: 
                 return await message.edit("[`THIS COMMAND ONLY FOR GROUP`]") 
             check = await message.chat.get_member(user_id) 
             is_admin = check.status==enums.ChatMemberStatus.ADMINISTRATOR 
             if not is_admin: 
                   return await message.edit("[`YOU ARE NOT ADMIN`]")
             elif not check.privileges.can_restrict_members:
                 return await message.edit("[`YOU CAN'T BAN PEOPLE'S HERE`]")
             return await func(app, message)                 
         return wrapped 




        
