""" SOME FUN MODULES FOR ENTERTAINMENT """


import config, asyncio 

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
    "**HACKING... COMPLE. **✅",
]
    for string in range(8):
          await asyncio.sleep(4)
          await message.edit(HACK_STRING[string % 8], parse_mode=enums.ParseMode.MARKDOWN)


__mod_name__ = "FUN"

__help__ = """
- hack: reply to the user
"""




string = {"module": __mod_name__, "help": __help__} 
MODULE.append(string)
