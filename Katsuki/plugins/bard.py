import httpx, config

from pyrogram import filters, errors
from Katsuki import app

@app.on_message(filters.me & filters.command('bard', prefixes=config.HANDLER))
async def google_bard(_, message):
    if not len(message.text.split()) >= 2:
        return await message.edit("I don't understand what you want?")
    
    query = message.text.split(None, 1)[1]
    if message.reply_to_message:
        text = (message.reply_to_message.text or message.reply_to_message.caption)
        prompt = f"{text}, note:{query}"
    elif len(message.text.split()) >= 2:
        prompt = query
    
    api = 'https://api.safone.me/bard'
    params = {"message": prompt}

    msg = await message.edit('Generating... please be patient')
    
    async with httpx.AsyncClient(timeout=10) as client:
        try:
            response = await client.get(api, params=params)
            response.raise_for_status()
            data = response.json()
            
            if bool(data['extras'][0]['images']):
                photo = data['extras'][0]['images'][0]
                try:
                    await message.reply_photo(photo=photo, caption=data['message'])
                    await msg.delete()
                except errors.MediaCaptionTooLong:
                    await msg.edit(data['message'])
            else:
                await msg.edit(data['message'])
        
        except httpx.TimeoutException:
            await msg.edit("The request timed out. Please try again later.")
        
        except httpx.HTTPError as e:
            await msg.edit(f"An HTTP error occurred: {str(e)}")
        
        except Exception as e:
            await msg.edit(f"An error occurred: {str(e)}")

