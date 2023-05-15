import wrapt

from pyrogram import enums
from pyrogram.types import Message 
from Katsuki import app


""" CHECK YOUR ACC HAS ADMIN IN CHAT """ 
  

def admin_only(func): 
         @wrapt.decorator 
         async def wrapped(client=app, message=Message): 
             chat_id=message.chat.id 
             user_id=message.from_user.id 
             if message.chat.type==enums.ChatType.PRIVATE: 
                 return await message.edit("[`THIS COMMAND NOT FOR GROUP`]") 
             check=await message.chat.get_member(user_id) 
             is_admin=check.status==enums.ChatMemberStatus.ADMINISTRATOR 
             if not is_admin: 
                 return await message.edit("[`YOU ARE NOT ADMIN`]")
             else: 
                 
                 return func(client=app, message=Message)  
               
         return wrapped 

        
