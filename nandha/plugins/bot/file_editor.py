import config
import time
import os


from nandha import bot, lang
from nandha.helpers.help_func import progress 
from moviepy.editor import VideoFileClip
from PIL import Image
from pyrogram import filters



                   
@bot.on_message(filters.command('rename'))
async def rename(_, message):
      reply = message.reply_to_message
      chat_id = message.chat.id
      if not reply:
            return await message.reply(lang['reply_to'])
      elif not reply.media:
            return await message.reply(lang['reply_to_media'])        
      else:
            message_id = reply.id
        
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
                        '**Download Complete.**'
            )
            dl_time = round(time.time()-start_dl, 2)
        
            start_ul = time.time()
            try:
                await bot.send_document(
                      chat_id=chat_id, 
                      document=path,
                      progress=progress,
                      progress_args=(msg, 'Uploading', start_ul)
            )
            except Exception as e:
                 return await msg.edit(
                   str(e)
                 )
                   
            ul_time = round(time.time()-start_ul, 2)
              
            return await msg.edit(
                        lang['rename_02'].format(dl_time, ul_time)
            )
                    
                                                             
@bot.on_message(filters.command('getgif'))
async def get_gif(_, message):
   reply = message.reply_to_message
   user_id = message.from_user.id
   if reply and reply.sticker and reply.sticker.is_video:
        msg = await message.reply('Wait, downloading...')
        path = await reply.download()
        clip = VideoFileClip(path)
        animation = f'{user_id}.gif'
        clip.write_gif(animation, fps=10)
        await msg.delete()
        return await message.reply_animation(
              animation=animation, quote=True
        )
   else:
       return await message.reply(
           'Reply to the Animated Sticker 🤔'
       )
             
        


  
@bot.on_message(filters.command('getsticker'))
async def get_sticker(_, message):
     reply = message.reply_to_message
     if reply:
        if reply.sticker and not reply.sticker.is_video:
              file = await reply.download(
              file_name=reply.sticker.file_name.split('.')[0]+'.png'
            )
              return await message.reply_document(
               file, quote=True
            )      
        elif reply.photo:
             file = await reply.download(
               file_name=reply.photo.file_unique_id+'.webp'
                )
             return await message.reply_sticker(
                file, quote=True
              )
        else:
            return await message.reply(
                lang['reply_to_media']
             )
     else:
         return await message.reply(
                lang['reply_to_media']
                )
      
        
  
__help__ = """
Cmds:
➩ /getsticker:
To get sticker at the same time you can change the image file to sticker formatt.
➩ /getgif: 
To convert a animated sticker to gif
➩ /rename: rename your any telegram file.
"""

__module__ = "Editor"




