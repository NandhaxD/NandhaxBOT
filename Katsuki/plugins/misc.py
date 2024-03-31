"""
Copyright © [2023-2024] @NandhaBots. All rights reserved. Reproduction, modification, distribution, or republication of this file without prior written permission from @NandhaBots is strictly prohibited. The Katsuki Telegram user bot has been developed with the Pyrogram library and utilizing Python programming language, making it a safe and secure option for users. Unauthorized use of this bot or any part of it may result in legal action. This project is owned by @Nandha, and any unauthorized use or distribution of this bot is strictly prohibited.
"""





import asyncio 
import config
import json
import os


from Katsuki import app, MODULE, bot, lang
from pyrogram import filters, enums
from gpytranslate import Translator
from urllib.parse import quote
import requests


copied_message = {}


@app.on_message(filters.command(['copy', 'clear'], prefixes=config.HANDLER))
async def copy_message(_, message):
    global copied_message
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


@app.on_message(filters.command('send', prefixes=config.HANDLER))
async def send_copied_message(_, message):
     if bool(copied_message):
           message_id = copied_message['message_id']
	   from_chat_id = copied_message['from_chat_id']
           await app.copy_message(message.chat.id, from_chat_id, message_id)
	   return await message.edit(lang['success'])


	

@app.on_message(filters.me & filters.command('alive', prefixes=config.HANDLER))
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
	
         
	         
@app.on_message(filters.me & filters.command("help", prefixes=config.HANDLER))
async def help_command(_, message):
      BOT_USERNAME = (await bot.get_me()).username
      query = "help"
      result = await app.get_inline_bot_results(bot=BOT_USERNAME, query=query)
      await app.send_inline_bot_result(chat_id=message.chat.id, query_id=result.query_id, result_id=result.results[0].id, reply_to_message_id=message.id)
      await message.delete()

@app.on_message(filters.me & filters.command("git",prefixes=config.HANDLER)) 
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




@app.on_message(filters.command(["ud","define"],prefixes=config.HANDLER) & filters.me)
async def ud(_, message):
        if len(message.command) < 2:
             return await message.edit("where you input the text?")         
        text = message.text.split(None, 1)[1]
        try:
          results = requests.get(
            f'https://api.urbandictionary.com/v0/define?term={text}').json()
          reply_text = f'<pre>Results:{text}</pre>\n\n<pre>{results["list"][0]["definition"]}\n\n{results["list"][0]["example"]}<pre>'
        except Exception as e: 
              return await message.edit_text(lang['error'].format(e))
        ud = await message.edit_text(lang['thinking'])
        await ud.edit_text(reply_text)
        
        
trans = Translator()
@app.on_message(filters.command("tr",prefixes=config.HANDLER) & filters.me)
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




__mod_name__ = "Misc"  
    
__help__ = """  
- git: find github user 
- tr {code}: reply to the message 
- ud: urban dictionary 
- tm: telegraph media upload
- txt: telegraph text upload
- paste: spacebin paste
- rename: rename a file with extension
"""  
    
    
string = {"module": __mod_name__, "help": __help__}   
MODULE.append(string)
