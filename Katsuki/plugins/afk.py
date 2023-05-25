



import config, strings
from pyrogram import filters
from Katsuki.helpers.help_func import get_datetime 
from Katsuki import app



DATA = {}









@app.on_message(filters.me & filters.command("afk", prefixes=config.HANDLER)) 
async def afk_turn_on(_, message): 
          if len(message.text.split()) >= 2: 
              reason = message.text.split(None,1)[1] 
          else: 
              reason = "Busy 🦥"
          date = await get_datetime()['date'] 
          time = await get_datetime()['time']           
          data = {'AFK': True, 'date': date,'time': time, 'reason': reason} 
          DATA.update(data) 
          return await message.edit('[`YOU TURN ON AFK NOW`]')
                                            
     
     

          


@app.on_message((filters.group | filters.private) & filters.me)
async def afk_turn_off(_, message): 
  
    try: 
          if DATA.get('AFK'): 
                    DATA.clear() 
                    return await message.reply_text("[`WELCOME BACK MASTER` 👾]") 
          else: return 
    except: pass
	      
	  	
	 
	 
@app.on_message(filters.group & filters.reply & ~filters.me)  
  async def telling_is_afk(_, message):  
               
           katsuki_id = 6129152989  
           try:  
                if not DATA.get('AFK'):  
                    return  
                elif message.reply_to_message.from_user.id == katsuki_id:  
                     date = DATA['date']  
                     time = DATA['time']  
                     reason = DATA['reason']  
                     return await message.reply_text(strings.AFK_STRING.format(  
                     reason=reason, date=date, time=time))        
            except: pass