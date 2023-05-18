

import config, strings
from Katsuki import app
from Katsuki.database import afk import (
add_afk, remove_afk, is_afk, get_afk_reason)
from pyrogram import filters, enums



@app.on_message(filters.me & filters.command("afk", config.HANDLER))
async def afk(_, message):
	
    user_id = message.from_user.id
    
	   
    if not len(message.text.split()) >= 2:
		 reason=random.choice(strings.REASON_STRING)
    else:
         reason = message.text.split(maxsplit=1)[1]
         
    datetime = datetime
    is_delete = False
    
    
    if (await is_afk(user_id)):
    	await remove_afk(user_id)
    	await add_afk(user_id=user_id, reason=reason, datetime=datetime, is_delete=is_delete)
    	return await message.edit("[`AFK UPDATED`]\n[`DELETE`: `{is_delete}`]", parse_mode=enums.ParseMode.MARKDOWN)
    else:
    	await add_afk(user_id=user_id, reason=reason, datetime=datetime, is_delete=is_delete)
    	return await message.edit(f"[`AFK ACTIVES`]\n[`DELETE`: `{is_delete}`]", parse_mode=enums.ParseMode.MARKDOWN)



@app.on_message(filters.me & filters.command("afkmod", config.HANDLER))   
async def afkmod(_, message):
      
      user_id = message.from_user.id
      
      pattern = [True, False]
      if len(message.text.split()) >= 2:
      	return await message.edit("[`INVALID`]")
      mm = message.text.split()[1]
      if not mm in pattern:
          	return await message.edit("[`INVALID`]")
      	
      is_delete = mm
      
      if (await is_afk(user_id)):
        	  await update_delete(user_id=user_id, is_delete=is_delete)
           return await message.edit(f"[`UPDATED`: `{is_delete}`]", parse_mode=enums.ParseMode.MARKDOWN)         
      else:      	
      	    return message.edit("[`NO ACTIVE AFK`]")



