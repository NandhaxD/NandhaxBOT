

"""
Copyright © [2023-2024] @NandhaBots. All rights reserved. Reproduction, modification, distribution, or republication of this file without prior written permission from @NandhaBots is strictly prohibited. The Katsuki Telegram user bot has been developed with the Pyrogram library and utilizing Python programming language, making it a safe and secure option for users. Unauthorized use of this bot or any part of it may result in legal action. This project is owned by @Nandha, and any unauthorized use or distribution of this bot is strictly prohibited.
"""





""" SOME FUN MODULES FOR ENTERTAINMENT """


import config, asyncio, requests 


from urllib.parse import quote
from Katsuki import app, MODULE 
from pyrogram import filters, enums





# Math tools

MATH_PERTTEN = ['cos', 'sin', 'tan', 'derive','integrate','simplify','factor']

@app.on_message(filters.me & filters.command(MATH_PERTTEN, prefixes=config.HANDLER))
async def mathematics(_, message):
     
     pertten = message.text[1:].split()[0]
     if not len(message.text.split()) >= 2:
           return await message.edit(f'{pertten} query')
     else:
         query = message.text.split(None,1)[1]
         query_req = quote(query)
         api = requests.get(f"https://newton.vercel.app/api/v2/{pertten}/{query_req}").json()
         result = api['result']
         if "Stop" in result:
              return await message.edit(lang['math_01'].format(pertten, query, result), parse_mode=enums.ParseMode.HTML)
         else:
              return await message.edit(lang['math_01'].format(pertten, query, result), parse_mode=enums.ParseMode.HTML)






__mod_name__ = "Fun"

__help__ = """

- maths: simplify, factor, integrate, derive
credit: https://newton.vercel.app/
"""




string = {"module": __mod_name__, "help": __help__} 
MODULE.append(string)
