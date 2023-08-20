
import config, strings, random
from time import time as Time 
from image import AFK_IMG
from pyrogram import filters, enums
from Katsuki.helpers.help_func import get_datetime 
from Katsuki import app



DATA = {}

AFK_STRING = ["I am currently AFK", "My apologies, I am away at the moment", "Unfortunately, I am not available at the moment", "My master is currently unavailable", "I am away from my keyboard", "Please excuse me, I am currently busy", "My master is temporarily offline", "I am currently occupied, please leave a message", "Sorry, I am currently not available", "Currently away from my computer", "Please leave a message as I am currently away", "My master is currently not present", "I am currently unavailable, sorry for the inconvenience", "My master is occupied at the moment", "Sorry, I am currently AFK and unable to respond"]




@app.on_message(filters.me & filters.command("afk", prefixes=config.HANDLER)) 
async def afk_turn_on(_, message): 
          
          if len(message.text.split()) >= 2: 
              if message.text.split()[1] == 'off':
                    DATA.clear()
                    return await message.edit("[`AFK TURN OFF`]")
              else:
                  reason = message.text.split(None,1)[1] 
          else: 
              reason = random.choice(AFK_STRING)
          await message.edit('[`YOU TURN ON AFK NOW`]')
          DATA.clear()
          seen = Time()
          date = (await get_datetime())['date'] 
          time = (await get_datetime())['time']           
          data = {'AFK': True, 'date': date,'time': time, 'reason': reason, 'seen': seen} 
          DATA.update(data) 
                                        
	 
@app.on_message((filters.group| filters.private) & filters.reply & ~filters.me, group=1)
async def telling_is_afk(_, message):  
               
           katsuki_id = config.OWNER_ID
           try:  
                if not DATA.get('AFK'):  
                    return  
                elif message.reply_to_message.from_user.id == katsuki_id:  
                     last_seen_time = Time() - DATA['seen']
                     last_seen_time = f"{last_seen_time * 1:.3f}s"
                     date = DATA['date']  
                     time = DATA['time']  
                     reason = DATA['reason']  
                     return await message.reply_photo(photo=AFK_IMG, caption=strings.AFK_STRING.format(  
                     reason=reason, date=date, time=time, seen=last_seen_time), parse_mode=enums.ParseMode.MARKDOWN)        
           except:
                 pass
