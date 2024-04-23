
from nandha import bot
from nandha.helpers.help_func import get_note_deatils, get_notes_list
from pyrogram import filters

right_format = 'Eg: `/save {notename} reply to text/media` or give text like `{notename} @nandha`'
exists = 'Note name already exist. delete and try again.'
added = 'Added `#{}`'

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
     if note_name in (await get_notes_list(chat_id)):
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

        
