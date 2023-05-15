import wrapt

from pyrogram import enums
from pyrogram.types import Message 
from Katsuki import app


""" CHECK YOUR ACC HAS ADMIN IN CHAT """ 
  

def admin_only(func): 
         @wrapt.decorator 
         async def wrapped(wrapped, client=app, message=Message, *args, **kwargs): 
             chat_id=message.chat.id 
             user_id=message.from_user.id 
             if message.chat.type==enums.ChatType.PRIVATE: 
                 return await message.edit("[`THIS COMMAND NOT FOR GROUP`]") 
             check=await message.chat.get_member(user_id) 
             is_admin=check.status==enums.ChatMemberStatus.ADMINISTRATOR 
             if is_admin: 
                 return True 
             else: 
                 return await message.edit("[`YOU ARE NOT ADMIN`]") 
             return func(wrapped, client: app, message: Message, *args, **kwargs) 
  
         return wrapped 

        
