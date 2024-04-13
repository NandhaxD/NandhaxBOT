import config
import time

from nandha import bot, lang
from nandha.helpers.help_func import progress 
from pyrogram import filters


                   
@bot.on_message(filters.command('rename'))
async def rename(_, message):
      reply = message.reply_to_message
      chat_id = message.chat.id
      message_id = reply.id
      if not reply:
            return await message.reply(lang['reply_to'])
      elif not reply.media:
            return await message.reply(lang['reply_to_media'])        
      else:
            if not len(message.text.split()) < 2:
                 file_name = message.text.split(None, 1)[1]
            else:
                return await message.reply(
                            lang['rename_01']
                )
            msg = await message.reply(
                        lang['download']
            )
            start_dl = time.time()
              
            path = await bot.download_media(
                    message=reply,
                    file_name=file_name, 
                    progress=progress,
                    progress_args=( 
                         msg, 'Downloading', start_dl)
                )
            
            await msg.edit(
                        'Download Complete.'
            )
            dl_time = round(time.time()-start_dl, 2)
        
            start_ul = time.time()
            await bot.send_document(
                      chat_id, 
                      document=path,
                      progress=progress,
                      progress_args=(msg, 'Uploading', start_ul)
            )
              
            ul_time = round(time.time()-start_ul, 2)
              
            return await msg.edit(
                        lang['rename_02'].format(dl_time, ul_time)
            )
                    
                                                             
      else:
         return await message.reply(
                     lang['reply_to_media']
         )
           
  
