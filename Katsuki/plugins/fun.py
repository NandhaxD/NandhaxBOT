

"""
Copyright © [2023-2024] @NandhaBots. All rights reserved. Reproduction, modification, distribution, or republication of this file without prior written permission from @NandhaBots is strictly prohibited. The Katsuki Telegram user bot has been developed with the Pyrogram library and utilizing Python programming language, making it a safe and secure option for users. Unauthorized use of this bot or any part of it may result in legal action. This project is owned by @Nandha, and any unauthorized use or distribution of this bot is strictly prohibited.
"""





""" SOME FUN MODULES FOR ENTERTAINMENT """


import config, asyncio, requests 

from Katsuki import app, MODULE 
from pyrogram import filters, enums


""" ANIMATION HACKS """
@app.on_message(filters.command("hack",config.HANDLER) & filters.me)
async def hack(_, message):
    
    if message.reply_to_message:
         user_id = message.reply_to_message.from_user.id
    else:
      return await message.edit("who should I hack ?")
    HACK_STRING = [
    "Looking for WhatsApp databases in targeted person...",
    "User online: True\nTelegram access: True\nRead Storage: True ",
    "Hacking... 20.63%\n`[███░░░░░░░░░░░░░░░░░]`",
    "Hacking... 56.21%\n`[█████████░░░░░░░░░░░]`",
    "Hacking... 86.21%\n`[███████████████░░░░░]`",
    "Hacking... 93.50%\n`[█████████████████░░░]`",
    "hacking...  100%\n`[████████████████████]`",
    "**HACK PROCESS COMPLE. **✅",
]
    for string in range(8):
          await asyncio.sleep(2)
          await message.edit(HACK_STRING[string % 8], parse_mode=enums.ParseMode.MARKDOWN)





""" MATH TOOLS """

@app.on_message(filters.me & filters.command('sfy', config.HANDLER))
async def simplify(_, message):
     if not len(message.text.split()) >= 2:
           return await message.edit('.sfy 2x - 3')
     else:
         query = message.text.split(None,1)[1]
         api = requests.get(f"https://newton.vercel.app/api/v2/simplify/{query}").json()
         result = api['result']
         if "Stop" in result:
             return await message.edit(f"**ERROR**:\n{result}")
         else:
            return await message.edit(f"**Result**:\{result}")






@app.on_message(filters.me & filters.command('factor', config.HANDLER)) 
 async def factor(_, message): 
      if not len(message.text.split()) >= 2: 
            return await message.edit('.factor x^2-1') 
      else: 
          query = message.text.split(None,1)[1] 
          api = requests.get(f"https://newton.vercel.app/api/v2/factor/{query}").json() 
          result = api['result'] 
          if "Stop" in result: 
              return await message.edit(f"**ERROR**:\n{result}") 
          else: 
             return await message.edit(f"**Result**:\{result}")

__mod_name__ = "FUN"

__help__ = """
- hack: reply to the user
- maths: simplify, factor 
"""




string = {"module": __mod_name__, "help": __help__} 
MODULE.append(string)
