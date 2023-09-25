import requests, config

from pyrogram import filters
from Katsuki import app

@app.on_message(filters.me & filters.command('bard', prefixes=config.HANDLER))
async def google_bard(_, message):
    
     # google bard AI 
   
    if message.reply_to_message:
        prompt = (message.reply_to_message.text or message.reply_to_message.caption)   
      
    elif len(message.text.split()) >= 2:
        prompt = message.text.split(None, 1)[1]
      
    else:
        return await message.edit('Type somthing bruh!')
      
    api = 'https://api.safone.me/bard'
    params = {"message": prompt}
    
    response = requests.get(api, params=params)

    msg = await message.edit('Generating... please patience')
        
    if response.ok:
         data = response.json()
         if not None data['images']:
              photo = data['images'][0]
              await message.reply_photo(photo, captain=data['message'])
              return await msg.delete()
         else:
             return await msg.edit(data['message'])
    else:
       return await msg.edit(response.status_code)
         
    
         
    
