



from nandha import app, bot
from nandha.helpers.function import send_auto_del_msg
from nandha.helpers.decorator import admin_rights
from pyrogram import filters, types


import config



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
      

     


                                
