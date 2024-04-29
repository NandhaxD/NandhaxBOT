

import random

from pyrogram import filters
from nandha import bot


CMDS = [ 'sex', 'boobs', 'dick', 'horny', 'gay', 'lezbian', 'noob', 'idiot', 'nigga' ] 

sex_string = [
  'Wanna sex with me? {}.',
  'Sorry you\'r pussy aren\'t that taste {}.'
]

@bot.on_message(filters.command(CMDS))
async def howall(_, message):
     reply = message.reply_to_message
     if reply:
         mention = reply.from_user.mention
     else:
         mention = reply.from_user.mention
     reply_func = reply.reply_animation if reply else message.reply_animation
     query = message.command[0]
     if query == 'sex':
        if reply:
           return await reply.reply_text(random.choice(sex_string.format(mention))                                  
        else:
           return await message.reply_text(random.choice(sex_string.format(mention))
     else:
          num = random.randint(0, 100)
          default = f'**You\'re {num}% {query} {mention}**'
          url_data = {
            'gay': 'https://telegra.ph//file/489199eab5a922b1e6529.mp4',
            'lezbian': 'https://telegra.ph//file/1d185a148783f364f1ee8.mp4',
            'horny': 'https://telegra.ph//file/1597814837d4f60d6944e.mp4',
            'dick': 'https://telegra.ph//file/3e270d488a6e09ea6e902.mp4',
            'boobs': 'https://telegra.ph//file/6cdb0450dcbc457a9e48f.mp4',
            'noob': 'https://telegra.ph//file/8e4d7e3213ab240f9df0b.mp4',
            'idiot': 'https://telegra.ph//file/71b56eee6b5f4b46d89bb.mp4',
            'nigga': 'https://telegra.ph//file/0e9acff8b61039a857d90.mp4'
          }
          if query in url_data:
             url = url_data[query]
             return await reply_func(
               animation=url, caption=default
             )
            
          
                                           


                                           
                                           
                                           





                                     



                                     

                                    
          
               
         
     
  
