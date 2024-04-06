import asyncio

from pyrogram import filters
from Katsuki import bot


loop = False

async def send_message(chat_id: int):
     count = 0
     while count < 10:
         if loop == False:
              return await bot.send_message(chat_id, 'loop was stopped!')
         elif count == 9:
              return await bot.send_message(chat_id, 'loop finished!')
         await bot.send_message(chat_id, f'hello {count}')
         await asyncio.sleep(7)
         count += 1

@bot.on_message(filters.user(5696053228) & filters.command('startloop'))
async def looptest(_, message):
     global loop

     if len(message.text.split()) < 2:
          return await message.reply('True or False?')
     condition = message.text.split(None, 1)[1]
     if bool(condition) == True:
          loop = True
          await send_message(chat_id=message.chat.id)
     elif bool(condition) == False:
          loop = False
          return await message.reply('loop stopping...')
  
     
