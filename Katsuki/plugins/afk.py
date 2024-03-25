import config, re
from Katsuki import app
from pyrogram import filters, enums, errors


AFK = {'afk': False, 'reason': None} 
@app.on_message(filters.me, group=10)
async def back_to_life(_, message):
      global AFK
      check = AFK['afk']
      if check:
           AFK['afk'] = False
           return await message.reply("<b>Welcome back by Katsuki ❤️!</b>")
           

@app.on_message(filters.me & filters.command('afk', prefixes=config.HANDLER), group=1)
async def away_from_keyboard(_, message):
     global AFK
     
     if len(message.command) <2:
           reason = None
     else:
           reason = message.text.split(None, 1)[1]
       
     AFK['afk'] = True
     AFK['reason'] = reason
     w = await message.reply('<b>You are now AFK!</b>')
     w.stop_propagation()
     return 


@app.on_message((filters.reply|filters.text) & ~filters.me ,group=3)  
async def afk_check(_, message):

        text = message.text
        pattern = r'@nandha\b'
        result = re.findall(pattern, text, re.IGNORECASE)
        r = message.reply_to_message
        IS_AFK = AFK['afk']
        try:
            if ((((r.from_user.id) == config.OWNER_ID) or result)
                   and IS_AFK):
                  reason = AFK['reason']
                  if reason is not None:
                        return await message.reply(
                          f'<pre>AFK: Away from keyboard!</pre>\n<pre>Reason:</pre><pre>{reason}</pre>', parse_mode=enums.ParseMode.HTML)
                  else:
                      return await message.reply('<b>Offline! ❤️ </b>')
        except errros.AttributeError:
                pass
        
                
