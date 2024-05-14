



from nandha import app
from nandha.helpers.function import send_auto_del_msg
from nandha.helpers.decorator import admin_rights
from pyrogram import filters, types


import config



@app.on_message(config.command('del'))
@admin_rights(bot, 'can_delete_messages')
async def delete_msg(_, message):
    reply = message.reply_to_message
    if reply:
         await reply.delete()
         await message.delete()
    else:
      return await send_auto_del_msg(
           bot,  chat_id, 
          '`Reply message to delete.`', message.id,  5)
      

     


                                
