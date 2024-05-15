



from nandha import app, bot
from nandha.helpers.function import send_auto_del_msg
from nandha.helpers.decorator import admin_rights
from pyrogram import filters, types


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


                                
