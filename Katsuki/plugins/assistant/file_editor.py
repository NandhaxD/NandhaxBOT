import config
import time

from Katsuki import bot, lang
from pyrogram import filters





async def progress(current, total, msg, type):
        if type = "dl":
            await msg.edit(f"Downloading... {c*100/t:.1f}%")
        elif type = "ul":
            await msg.edit(f"Uploading... {c*100/t:.1f}%")
        return 
                   
@bot.on_message(filters.reply & filters.commamd('rename', prefixes=config.HANDLER))
async def rename(_, message):
      reply = message.reply_to_message
      chat_id = message.chat.id
      message_id = reply.id
  
      if bool(reply.media):
            if not len(message.text.split()) < 2:
                 file_name = message.text.split(None, 1)[1]
            else:
                return await message.reply('Give File Name!')
            msg = await message.reply(lang['download'])
            start_dl = time.time()
            path = await bot.download_media(
                    message=reply,
                    file_name=file_name, 
                    progress=progress( 
                         current, total, msg, type='dl')
                )
            
            await msg.edit('Download Complete.')
            dl_time = round(time.time-start_dl, 3)
        
            start_ul = time.time()
            await bot.send_document(
                      chat_id, 
                      document=path,
                      progress=progress(current, total, msg, type='ul'))
            ul_time = round(time.time-start_ul, 3)
            await msg.edit(
                  f"download taken time: {dl_time}"
                  f"upload taken time: {ul_time}"
                  f"thank you for using me. (:"
            )
                       
              
            
            
      else:
         return await message.reply('Reply To Document, Media!')
           
  
