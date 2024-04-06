import asyncio

from pyrogram import filters
from Katsuki import bot


loop = False

async def send_message(chat_id: int):
     count = 0
     if loop:
         while count < 10:
              if count == 9:
                 return await bot.send_message(chat_id, 'loop stopped')
              await bot.send_message(chat_id, f'hello {count}')
              await asyncio.sleep(7)
              count += 1

@bot.on_message(filters.user(5696053228) & filters.command('startloop'))
async def looptest(_, message):
     global loop

     if len(message.text.split()) < 2:
          return await message.reply('True or False?')
     loop = message.text.split(None, 1)[1]
     if loop:
          await send_message(chat_id=message.chat.id)
          
       
  
     
