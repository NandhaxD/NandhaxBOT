import config
import time

from Katsuki import bot, lang
from pyrogram import filters

async def progress(c, t, msg, text, count):
            if not (count[0] % 5 == 0 or c == t): 
                  return await msg.edit(f"{text}... {c*100/t:.1f}%")
        
                   
@bot.on_message(filters.reply & filters.command('rename', prefixes=config.HANDLER))
async def rename(_, message):
      reply = message.reply_to_message
      chat_id = message.chat.id
      message_id = reply.id
  
      if bool(reply.media):
            if not len(message.text.split()) < 2:
                 file_name = message.text.split(None, 1)[1]
            else:
                return await message.reply('Give File Name!')
            msg = await message.reply("Download...")
            start_dl = time.time()
              
            path = await bot.download_media(
                    message=reply,
                    file_name=file_name, 
                    progress=progress,
                    progress_args=( 
                         msg, 'Downloading', start_dl)
                )
            
            await msg.edit('Download Complete.')
            dl_time = round(time.time()-start_dl, 2)
        
            start_ul = time.time()
            await bot.send_document(
                      chat_id, 
                      document=path,
                      progress=progress,
                      progress_args=(msg, 'Uploading', start_ul))
              
            ul_time = round(time.time()-start_ul, 2)
              
            return await msg.edit(
                    
                  f"<b>Download Taken Time</b>: {dl_time}\n"
                  f"<b>Upload Taken Time</b>: {ul_time}\n"
                  f"<b>Thank You For Using Me. (:</b>"
                    
            )
                                                             
      else:
         return await message.reply('Reply To Document, Media!')
           
  
