
from nandha import bot
from nandha.helpers.help_func import get_note_deatils
from pyrogram import filters

right_format = 'Eg: `/save {notename} reply to text/media` or give text like `{notename} @nandha`'
cant_encode = 'sorry i cannot encode the string maybe try removing some unicodes strings in text.'
@bot.on_message(filters.command('save'))
async def save_note(_, message):
     
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
               
     return await message.reply(note)

        
