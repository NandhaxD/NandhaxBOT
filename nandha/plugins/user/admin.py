



from nandha import app, bot
from nandha.helpers.function import send_auto_del_msg
from nandha.helpers.decorator import admin_rights
from nandha.helpers.help_func import match_text
from pyrogram import filters, types, enums


import config
import time



@app.on_message(filters.me & config.command('del'))
@admin_rights('can_delete_messages')
async def delete_msg(client, message):

    chat_id = message.chat.id
    reply = message.reply_to_message
    if reply:
         await reply.delete()
         await message.delete()
    else:
      ask = '`Reply message to delete.`'
      return await send_auto_del_msg(
           client=client,
           method='message', 
           chat_id=chat_id, 
           text=ask,
           reply_to_message_id=message.id, 
           time=5)
      


@app.on_message(filters.me & config.command('purge'))
@admin_rights('can_delete_messages')
async def purge_msg(client, message):

      chat_id = message.chat.id
      reply = message.reply_to_message
      if reply:
           reply_msg_id = reply.id
           message_id = message.id
           msg_ids = []
           start = time.time()
           for id in range(reply_msg_id, message_id+1):
                msg_ids.append(id)
           try:
             dels = await client.delete_messages(
                  chat_id, message_ids=msg_ids
              )
           except Exception as e:
               return await message.reply(str(e))
           taken_time = round(time.time() - start, 3)
           text = f"**Successfully deleted {dels} message's in {message.chat.title}\nTaken time: {taken_time}**" 
           return await send_auto_del_msg(
              client=client,
              method='message', 
              chat_id=chat_id, 
              text=text,
              reply_to_message_id=message.id, 
              time=5)          
      else:
         ask = '`Reply message to purge.`'
         return await send_auto_del_msg(
           client=client,
           method='message', 
           chat_id=chat_id, 
           text=ask,
           reply_to_message_id=message.id, 
           time=5)


@app.on_message(filters.me & config.command('ban'))
@admin_rights('can_restrict_members')
async def ban_member(client, message):

      chat_id = message.chat.id
      if message.chat.type == enums.ChatType.PRIVATE:
            return await message.reply(
                'You cannot use in private.')

      reply = message.reply_to_message
    
      if len(message.text.split()) == 2:
           user_id = message.text.split()[1]          
      elif reply:
           user_id = reply.sender_chat.id if reply.sender_chat else reply.from_user.id
      else:
          ask = "Reply to the user or give the user name/id to ban."
          return await send_auto_del_msg(
           client=client,
           method='message', 
           chat_id=chat_id, 
           text=ask,
           reply_to_message_id=message.id, 
           time=5)
        
      info = await client.get_chat(user_id)
      name = info.first_name if info.first_name else info.title
      user_id = info.id
      
      try:
          await client.ban_chat_member(chat_id, user_id)
      except Exception as e:
           return await message.reply(str(e))
      text = f"**{name} banned in {message.chat.title}.**"
      return await message.reply(
        text=text)
     

@app.on_message(filters.me & config.command('unban'))
@admin_rights('can_restrict_members')
async def ban_member(client, message):

      chat_id = message.chat.id
      if message.chat.type == enums.ChatType.PRIVATE:
            return await message.reply(
                'You cannot use in private.')

      reply = message.reply_to_message
    
      if len(message.text.split()) == 2:
           user_id = message.text.split()[1]          
      elif reply:
           user_id = reply.sender_chat.id if reply.sender_chat else reply.from_user.id
      else:
          ask = "Reply to the user or give the user name/id to unban."
          return await send_auto_del_msg(
           client=client,
           method='message', 
           chat_id=chat_id, 
           text=ask,
           reply_to_message_id=message.id, 
           time=5)
        
      info = await client.get_chat(user_id)
      name = info.first_name if info.first_name else info.title
      user_id = info.id
      
      try:
          await client.unban_chat_member(chat_id, user_id)
      except Exception as e:
           return await message.reply(str(e))
      text = f"**{name} unbanned in {message.chat.title}.**"
      return await message.reply(
        text=text)

            
            
@app.on_message(filters.me & config.command(['promote', 'fpromote']))
@admin_rights('can_promote_members')
async def promote_member(client, message):

      chat_id = message.chat.id
    
      if message.chat.type == enums.ChatType.PRIVATE:
            return await message.reply(
                'You cannot use in private.')
          
      reply = message.reply_to_message
      
      if len(message.text.split()) == 2:
            user_id = message.text.split()[1]
        
      elif reply:
            user_id = reply.from_user.id
        
      else:
           ask = "promote the user by replying the user or give id/name."
           return await send_auto_del_msg(
           client=client,
           method='message', 
           chat_id=chat_id, 
           text=ask,
           reply_to_message_id=message.id, 
           time=5)

      user_info = await client.get_users(user_id)
      user_id = user_info.id
      name = user_info.first_name

      cmd = message.command[0]
      text = f"**{name} Successfully {cmd.upper()} in {message.chat.title}.**"

      
      if match_text('fpromote', cmd):
           
           privileges = (await client.get_chat_member(
                 chat_id=chat_id, 
                 user_id=client.me.id)).privileges
           try:
              await client.promote_chat_member(
                   chat_id=chat_id, user_id=user_id, privileges=privileges)
           except Exception as e:
                return await message.reply(str(e))
           return await message.reply(
               text=text)
      
      elif match_text('promote', cmd):
           
           privileges = types.ChatPrivileges(
               can_delete_messages=True,
               can_manage_video_chats=True,
               can_restrict_members=True,
               can_invite_users=True,
               can_pin_messages=True)
        
           try:
              await client.promote_chat_member(
                   chat_id=chat_id, user_id=user_id, privileges=privileges)
           except Exception as e:
                return await message.reply(str(e))
           return await message.reply(
               text=text)
             
             
           



@app.on_message(filters.me & config.command('demote'))
@admin_rights('can_promote_members')
async def demote_member(client, message):

      chat_id = message.chat.id
    
      if message.chat.type == enums.ChatType.PRIVATE:
            return await message.reply(
                'You cannot use in private.')
          
      reply = message.reply_to_message
      
      if len(message.text.split()) == 2:
            user_id = message.text.split()[1]
        
      elif reply:
            user_id = reply.from_user.id
        
      else:
           ask = "Demote the admin by replying the admin or give id/name."
           return await send_auto_del_msg(
           client=client,
           method='message', 
           chat_id=chat_id, 
           text=ask,
           reply_to_message_id=message.id, 
           time=5)

      user_info = await client.get_users(user_id)
      user_id = user_info.id
      name = user_info.first_name

      cmd = message.command[0]
      text = f"**{name} Successfully {cmd.upper()} in {message.chat.title}.**"

      privileges = types.ChatPrivileges(
               can_change_info=False,
               can_delete_messages=False,
               can_manage_video_chats=False,
               can_restrict_members=False,
               can_invite_users=False,
               can_pin_messages=False,
        
               )

      try:
          await client.promote_chat_member(
                 chat_id=chat_id,
                 user_id=user_id,
                 privileges=privileges)
      except Exception as e:
           return await message.reply(str(e))
      return await message.reply(
           text=text)
              
    



                                
