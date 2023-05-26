"""
Copyright © [2023-2024] @NandhaBots. All rights reserved. Reproduction, modification, distribution, or republication of this file without prior written permission from @NandhaBots is strictly prohibited. The Katsuki Telegram user bot has been developed with the Pyrogram library and utilizing Python programming language, making it a safe and secure option for users. Unauthorized use of this bot or any part of it may result in legal action. This project is owned by @Nandha, and any unauthorized use or distribution of this bot is strictly prohibited.
"""





import asyncio 
import config

from Katsuki import app, MODULE, INFO
from pyrogram import filters, enums
from gpytranslate import Translator

import requests


 

AI = False


@app.on_message(filters.me & filters.command("ai", config.HANDLER))
async def chatbot_turn_on(_, message ):
	 global AI
 
	 pertten = ['on', 'off']
	 if not len(message.text.split() >= 2:
	 	 return await message.edit('pertten: on|off')
         query = message.text.split()[1]
         if not query in pertten:
     	       return await message.edit('pertten: on|off')
         else:
 
     	      if query == 'on':
     		      AI = True
                  return await message.edit('`AI MOD TRUN ON`')              
              elif query == 'off':
                   AI = False
                   return await message.edit('`AI MOD TRUN OFF`')
     		  
     		  
FILTERS = (filters.group | filters.private) & ~filters.me & ~filters.bot & filters.text & filters.reply
	
	

@app.on_message(FILTERS)
async def chatbot(_, message):	
    try:
        
       katsuki_id = 6129152989
       if AI is True and message.reply_to_message.from_user.id == katsuki_id:
      	url = f"https://kora-api.vercel.app/chatbot/2d94e37d-937f-4d28-9196-bd5552cac68b/Nandha/Nandha/message={message.text}"
      	response = requests.get(url)
          results = json.loads(response.text)
          content = results['reply']
          await message.reply(content, quote=True)
    except:
     	 pass



	         
@app.on_message(filters.me & filters.command("help", prefixes=config.HANDLER))
async def help_command(_, message):
      BOT_USERNAME = (await INFO.bot()).id
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
          reply_text = f'**results: {text}**\n\n{results["list"][0]["definition"]}\n\n_{results["list"][0]["example"]}_'
        except Exception as e: 
              return await message.edit_text(f"Somthing wrong Happens:\n`{e}`")
        ud = await message.edit_text("[`EXPLORING`]")
        await ud.edit_text(reply_text)
        
        
trans = Translator()
@app.on_message(filters.command("tr",prefixes=config.HANDLER) & filters.me)
async def translate(_, message) -> None:
    reply_msg = message.reply_to_message
    if not reply_msg:
        await message.reply_text("[Reply To The Message Using The Translation Code Provided!](https://telegra.ph/Lang-Codes-03-19-3)")
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
    reply = (
        f"**Translated from {source} to {dest}**:\n"
        f"`{translation.text}`"
    )
    await message.delete()
    await reply_msg.reply_text(reply)
    return 




__mod_name__ = "MISC"  
    
__help__ = """  
- git: find github user 
- tr {code}: reply to the message 
- ud: urban dictionary 
- write: unruled-note handwriting
- tm: telegraph media upload
- txt: telegraph text upload
- paste: spacebin paste
- rename: rename a file with extension
"""  
    
    
string = {"module": __mod_name__, "help": __help__}   
MODULE.append(string)
