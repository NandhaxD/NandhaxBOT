"""
Copyright © [2023-2024] @NandhaBots. All rights reserved. Reproduction, modification, distribution, or republication of this file without prior written permission from @NandhaBots is strictly prohibited. The Katsuki Telegram user bot has been developed with the Pyrogram library and utilizing Python programming language, making it a safe and secure option for users. Unauthorized use of this bot or any part of it may result in legal action. This project is owned by @Nandha, and any unauthorized use or distribution of this bot is strictly prohibited.
"""





import asyncio 
import config
import json
import os
import time
import base64


from nandha import app, MODULE, bot, lang, StartTime
from nandha.helpers.help_func import grap, get_readable_time, make_carbon
from pyrogram import filters, enums
from gpytranslate import Translator
from urllib.parse import quote
import requests



@app.on_message(filters.me & filters.command('ping', prefixes=config.PREFIXES))
async def ping(_, message):
	start = time.time()
	uptime = get_readable_time(time.time()-StartTime)
	ping = round(time.time() - start, 3)
	msg = await message.edit(
		'**🏓 🏓 Pinging....**'
	)
	await msg.edit(
		f'🏓 **Ping**: {ping}ms\n**⏲️ Uptime**: {uptime}'
	)
	



@app.on_message(filters.me & filters.command('cb', prefixes=config.PREFIXES))
async def carbon(_, message):
	reply = message.reply_to_message
	if not reply:
             msg = await message.edit(lang['reply_to'])
	     await asyncio.sleep(10)
	     return await msg.delete()
	else:
	    try:
	      query = message.text.split(None, 1)[1]
	      msg = await message.edit(lang['alyz'])
	      image = await make_carbon(query)
	      await message.reply_photo(photo=image)
	      await msg.delete()    
	    except Exception as e:
		     return await message.edit(lang['error'].format(e))

copied_message = {}

@app.on_message(~filters.bot & filters.me & filters.command(['copy', 'clear'], prefixes=config.PREFIXES))
async def copy_message(_, message):
    reply = message.reply_to_message
    if message.text.split()[0][1:].lower() == 'clear':
        return await message.edit(lang['success'])
       
    if not reply:
        return await message.reply(lang['reply_to'])
    else:
        message_id = reply.id
        from_chat = message.chat.id
        format = {'from_chat_id': from_chat, 'message_id': message_id}
	    
        copied_message.update(format)
        return await message.edit(lang['copied'])

@app.on_message(~filters.bot & filters.me & filters.command('paste', prefixes=config.PREFIXES))
async def send_copied_message(_, message):
    if bool(copied_message):
        message_id = copied_message['message_id']
        from_chat_id = copied_message['from_chat_id']
        await app.copy_message(message.chat.id, from_chat_id, message_id)
        return await message.edit(lang['success'])
	    

	
@app.on_message(filters.me & filters.command('alive', prefixes=config.PREFIXES))
async def alive(_, message):
    await message.edit(lang['alive'])


#ai_models = { 'bard': 'gemini', 'gpt': 'chatgpt' }


@app.on_message(filters.me & filters.command(['bard','gpt', 'palm'], prefixes=""))
async def artificial_intelligent(_, message):
	
	if len(message.command) <2:
		return await message.edit(lang['query'])
        
	reply = await message.edit(lang['thinking'])
	model = message.text.split()[0]
	#model = ai_models[model]
	prompt = message.text.split(None, 1)[1]
	api = f"https://nandha-api.onrender.com/ai/{model}/{quote(prompt, safe='')}"	
	#api = f"https://tofu-node-apis.onrender.com/api/{model}?prompt={quote(prompt, safe='')}"	
	try:		
	    response = requests.get(api).json()
	    ok = response.get('content')		
	except Exception as e:
		 return await reply.edit(lang['error'].format(str(e)), parse_mode=enums.ParseMode.HTML)				
	return await reply.edit(lang['AI'].format(model.upper(), prompt, ok), parse_mode=enums.ParseMode.HTML)
	
         


@app.on_message(filters.me & filters.command("git",prefixes=config.PREFIXES)) 
async def github(_, message): 
     if len(message.command) < 2: 
         return await message.edit_text("where you input the username?\n") 
     user = message.text.split(None, 1)[1] 
     res = requests.get(f'https://api.github.com/users/{user}').json() 
     data = f"""**Name**: {res['name']} 
 **UserName**: {res['login']} 
 **Link**: [{res['login']}]({res['html_url']}) 
 **Bio**: {res['bio']} 
 **Company**: {res['company']} 
 **Blog**: {res['blog']} 
 **Location**: {res['location']} 
 **Public Repos**: {res['public_repos']} 
 **Followers**: {res['followers']} 
 **Following**: {res['following']} 
 **Acc Created**: {res['created_at']} 
 """ 
     with open(f"{user}.jpg", "wb") as f: 
         kek = requests.get(res['avatar_url']).content 
         f.write(kek) 
  
     await message.reply_document(f"{user}.jpg", caption=data, quote=True) 
     os.remove(f"{user}.jpg") 
     await message.delete() 
     return 




@app.on_message(filters.command(["ud","define"],prefixes=config.PREFIXES) & filters.me)
async def ud(_, message):
        if len(message.command) < 2:
             return await message.edit("where you input the text?")         
        text = message.text.split(None, 1)[1]
        try:
          results = requests.get(
            f'https://api.urbandictionary.com/v0/define?term={text}').json()
          reply_text = f'<pre>Results:{text}</pre>\n\n<pre>{results["list"][0]["definition"]}\n\n{results["list"][0]["example"]}</pre>'
        except Exception as e: 
              return await message.edit_text(lang['error'].format(e))
        ud = await message.edit_text(lang['thinking'])
        await ud.edit_text(reply_text)
        
        
trans = Translator()
@app.on_message(filters.command("tr",prefixes=config.PREFIXES) & filters.me)
async def translate(_, message) -> None:
    reply_msg = message.reply_to_message
    if not reply_msg:
        await message.reply_text(lang['translate_01'])
        return
    if reply_msg.caption:
        to_translate = reply_msg.caption
    elif reply_msg.text:
        to_translate = reply_msg.text
    try:
        args = message.text.split()[1].lower()
        if "//" in args:
            source = args.split("//")[0]
            dest = args.split("//")[1]
        else:
            source = await trans.detect(to_translate)
            dest = args
    except IndexError:
        source = await trans.detect(to_translate)
        dest = "en"
    translation = await trans(to_translate, sourcelang=source, targetlang=dest)
    await message.delete()
    await reply_msg.reply_text(lang['translate_02'].format(source, dest, translation.text))
    return 



data = {
  "type": "quote",
  "format": "webp",
  "backgroundColor": None,
  "width": 512,
  "height": 768,
  "scale": 2,
  "messages": [
    {
      "entities": [],
      "avatar": True,
      "from": {
        "id": 1,
        "name": None,
        "photo": {
          "url": None
        }
      },
      "text": None,
      "replyMessage": {}
    }
  ]
}


@app.on_message(filters.me & filters.command(['q','quote'], prefixes=config.PREFIXES))
async def quote_ub(_, message):
           reply = message.reply_to_message
           if (reply and reply.forward_from):
                if not len(message.text.split()) < 2:
                      bg_code = message.text.split()[1]
                else:
                     bg_code = "332255"
                text = reply.text if reply.text else None
                photo_id = reply.forward_from.photo.big_file_id if reply.forward_from.photo else "AgACAgUAAxkDAAECAW9mCc9TJA-yyVyZ12RsrE2MAyr1YAACx7oxGz2WUVRbAAGQzuS-v5UACAEAAwIAA3gABx4E"
                username = reply.forward_from.first_name
                avatar_url = await grap(await app.download_media(photo_id))
                
           elif reply:
                 if not len(message.text.split()) < 2:
                       bg_code = message.text.split()[1]
                 else:
                       bg_code = "332255"
                 text = reply.text if reply.text else None
                 if text is None:
                     return await message.reply(lang['reply_to_text'])
                 photo_id = reply.from_user.photo.big_file_id if reply.from_user.photo else "AgACAgUAAxkDAAECAW9mCc9TJA-yyVyZ12RsrE2MAyr1YAACx7oxGz2WUVRbAAGQzuS-v5UACAEAAwIAA3gABx4E"
                 username = reply.from_user.first_name
                 avatar_url = await grap(await app.download_media(photo_id))
          
           elif not reply:
               if not len(message.text.split()) < 2:
                   try:
                        bg_code = message.text.split(message.text.split()[0])[1].split('|')[0]
                        is_bg_code = True
                   except:
                        bg_code = "332255"
                    
                   text = message.text.split(message.text.split()[0])[1].split('|')[1] if is_bg_code == True else message.text.split(None, 1)[1]
                   username = message.from_user.first_name
                   photo_id = message.from_user.photo.big_file_id if message.from_user.photo else "AgACAgUAAxkDAAECAW9mCc9TJA-yyVyZ12RsrE2MAyr1YAACx7oxGz2WUVRbAAGQzuS-v5UACAEAAwIAA3gABx4E"
                   avatar_url = await grap(await app.download_media(photo_id))
           else:
               return await message.edit(lang['quote'])

           data['backgroundColor'] = bg_code
           data['messages'][0]['from']['name'] = username
           data['messages'][0]['from']['photo']['url'] = avatar_url
           data['messages'][0]['text'] = text
           response = requests.post('https://bot.lyo.su/quote/generate', json=data).json()
           buffer = base64.b64decode(response['result']['image'].encode('utf-8'))
           name = f"{username}.webp"
           open(name, 'wb').write(buffer)
           return await message.reply_sticker(sticker=name, quote=True)

	

__mod_name__ = "Misc"  
    
__help__ = """  
- git: find github user 
- q: for quote msg
- tr {code}: reply to the message 
- ud: urban dictionary 
- tm: telegraph media upload
- txt: telegraph text upload
- paste: spacebin paste
- ping: check ping&uptime
"""  
    
    
string = {"module": __mod_name__, "help": __help__}   
MODULE.append(string)
