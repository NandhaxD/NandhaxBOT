
import config

from nandha import bot
from nandha.helpers.help_func import get_note_deatils
from nandha.database.notes import get_notes_list, add_note, get_note
from pyrogram import filters

right_format = 'Eg: `/save {notename} reply to text/media` or give text like `{notename} @nandha`'
exists = '**Note name already exist. delete and try again.**'
added = 'Added!:`{}`\nGet the note using `/get notename`'

get_note_eg = 'Example:\n`/get {notename}`'


@bot.on_message(filters.command('get', prefixes=config.PREFIXES))
async def get_note(_, message):
      chat_id = message.chat.id
      reply = message.reply_to_message
     
      if len(message.text.split()) < 2:
            return await message.reply(
                 get_note_eg
            )   
      else:
          note_name = message.text.split()[1]
          note = await get_note(
               chat_id=chat_id,
               name=note_name
          )
          note = notes[0]
          type = note.get('type', '')
          file_id = note.get('file_id', '')
          caption = note.get('caption', None)
          text = note.get('text', '')


          if type == '#STICKER':
               reply_func = reply.reply_sticker if reply else message.reply_sticker
               return await reply_func(file_id)
          elif type == '#PHOTO':
               reply_func = reply.reply_photo if reply else message.reply_photo
               return await reply_func(
                    photo=file_id, 
                    caption=caption
               )
          elif type == '#TEXT':
                reply_func = reply.text if reply else message.reply_text
                return reply_func(
                     text=text
                )
          elif type == '#ANIMATION':
                reply_func = reply.animation if reply else message.reply_animation
                return reply_func(
                     animation=file_id, 
                     caption=caption
                )
          elif type == '#DOCUMENT':
                reply_func = reply.document if reply else message.reply_document
                return reply_func(
                     document=file_id, 
                     caption=caption
                )
          elif type == '#VIDEO':
                reply_func = reply.video if reply else message.reply_video
                return reply_func(
                     video=file_id, 
                     caption=caption
                )
          

          

     
     

 

      
      








@bot.on_message(filters.command('save'))
async def save_note(_, message):

     chat_id = message.chat.id
     
     reply = message.reply_to_message
  
     if not reply:
         if len(message.text.split()) <= 2:
             return await message.reply(
                  right_format
             )
     elif reply:
          if len(message.text.split()) < 2:
              return await message.reply(
                 right_format
              )
     try:
        note = await get_note_deatils(message)
     except Exception as e:
          return await message.reply(
               str(e)
          )
               
     note_name = note['name']
     notes_list = await get_notes_list(chat_id)
     if (not notes_list is None) and (note_name in notes_list):
          return await message.reply(
                 exists
          )
     else:
           await add_note(
                chat_id=chat_id, 
                data=note
           )
           return await message.reply(
                added.format(note_name)
           )

        
