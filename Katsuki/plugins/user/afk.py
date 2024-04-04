import config 

from Katsuki import app, lang
from pyrogram import filters, enums, errors


AFK = {'afk': False, 'reason': None} 
afk_url = "https://graph.org/file/cc5d46b2d63dc1ebbe3f3.mp4"

@app.on_message(filters.me, group=10)
async def back_to_life(_, message):
      global AFK
      check = AFK['afk']
      if check:
           AFK['afk'] = False
           return await message.reply(lang['afk_04'])
           

@app.on_message(filters.me & filters.command('afk', prefixes=config.HANDLER), group=1)
async def away_from_keyboard(_, message):
     global AFK
     
     if len(message.command) <2:
           reason = None
     else:
           reason = message.text.split(None, 1)[1]
       
     AFK['afk'] = True
     AFK['reason'] = reason
     w = await message.reply(lang['afk_01'])
     w.stop_propagation()
     return 


@app.on_message(filters.reply & ~filters.me & ~filters.bot ,group=3)  
async def afk_check(_, message):
      
        r = message.reply_to_message
        IS_AFK = AFK['afk']
        try:
            if (((r.from_user.id) == config.OWNER_ID) and IS_AFK):
                  reason = AFK['reason']
                  if reason is not None:
                        return await message.reply_animation(animation=afk_url, caption=lang['afk_02'].format(reason), quote=True)
                  else:
                       return await message.reply_animation(animation=afk_url, caption=lang['afk_03'], quote=True)
            
        except AttributeError:
                pass
        
                
