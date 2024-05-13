import config 
import random


from nandha import app, lang
from nandha.helpers.help_func import get_anime_gif, anime_gif_key, get_datetime
from pyrogram import filters, enums, errors




AFK = {'afk': False, 'reason': None, 'datetime': None} 



say_afk = [
      '**Bye Bye. {}.**',
      '**Okay {} take some rest.**',
      '**Nice take care {}**',
      '**Take your time {}**'
]

say_welcome = [
      '**Hey {} is Back!**',
      '**Whats up {}!, are you done?**',
      '**{} is back online**',
      '**yeahh {} is came!**'
]

@app.on_message(filters.me, group=2)
async def back_to_online(_, message):
      global AFK
      check = AFK['afk']
      if check:
           AFK['afk'] = False
           name = message.from_user.mention
           return await message.reply(say_welcome.format(name))
           

@app.on_message(filters.me & filters.command('afk', prefixes=config.PREFIXES), group=1)
async def away_from_keyboard(_, message):
     global AFK
     
     if len(message.command) <2:
        reason = None
     else:
        reason = message.text.split(None, 1)[1]

      
     datetime = await get_datetime()
     AFK['afk'] = True
      
     AFK['datetime'] = datetime['date'] + ' ' + datetime['time']
     AFK['reason'] = reason
     mention = message.from_user.mention
     w = await message.reply(
           random.choice(say_afk).format(mention))
     w.stop_propagation()
     return 


@app.on_message(filters.reply & ~filters.me & ~filters.bot ,group=-1)  
async def afk_check(_, message):
      
        r = message.reply_to_message
        IS_AFK = AFK['afk']
        try:
            if (((r.from_user.id) == config.OWNER_ID) and IS_AFK):
                  reason = AFK['reason']
                  name = message.from_user.mention
                  text = f'**{name}, My master is offline.**'
                  datetime = AFK['datetime']
                  if reason:
                        text += f'\n**🥸 Reason**: `{reason}`'
                  if datetime:
                        text += f'\n**📛 Since**: `{datetime}`'
                  url = await get_anime_gif(anime_gif_key[2])
                  return await message.reply_animation(
                              animation=url, 
                              caption=text, quote=True
                        )                                                              
        except AttributeError:
                pass
        
                
