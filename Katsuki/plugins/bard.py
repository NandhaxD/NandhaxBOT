import requests, config

from pyrogram import filters, errors
from Katsuki import app

@app.on_message(filters.me & filters.command('bard', prefixes=config.HANDLER))
async def bard_ai(_, message):
    
     # google bard AI 
    if not len(message.text.split()) >= 2:
          return await message.edit("`.bard hello`")
                                    
    query = message.text.split(None, 1)[1]
    if message.reply_to_message:
        text = (message.reply_to_message.text or message.reply_to_message.caption)
        prompt = f"{text}, Note:{query}"
      
    elif len(message.text.split()) >= 2:
         prompt = query 
    
      
    api = 'https://api.safone.me/bard'
    params = {"message": prompt}

    msg = await message.edit('Generating... please patience')
        
    response = requests.get(api, params=params)

    
    if response.ok:
         data = response.json()
         if bool(data['extras'][0]['images']) == True:
              photo = data['extras'][0]['images'][0]
              try:
                 await message.reply_photo(photo=photo, caption=data['message'])
                 return await msg.delete()
              except errors.MediaCaptionTooLong:
                     return await msg.edit(data['message'])
         else:
             return await msg.edit(data['message'])
    else:
       return await msg.edit(response.status_code)
    
