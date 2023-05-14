import asyncio 
import config

from Katsuki import app
from pyrogram import filters
from gpytranslate import Translator

import requests

@app.on_message(filters.me & filters.command("git",prefixes=config.HANDLER)) 
async def git(_, message): 
     if len(message.command) < 2: 
         return await message.reply_text("where you input the username?\n") 
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
         kek = get(res['avatar_url']).content 
         f.write(kek) 
  
     await message.reply_photo(f"{user}.jpg", caption=data, quote=True) 
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
        ud = await message.edit_text("Exploring....", quote=True)
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
    
__help__ = """\n  
- git: find github user 
- tr {code}: reply to the message 
- ud: urban dictionary 
- write: unruled-note handwriting
- tm: telegraph upload
"""  
    
    
string = {"module": __mod_name__, "help": __help__}   
MODULE.append(string)