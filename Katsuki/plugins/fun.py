""" SOME FUN MODULES FOR ENTERTAINMENT """


import config, asyncio 

from Katsuki import app
from pyrogram import filters


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
    "Hacking... 20.63%\n[███░░░░░░░░░░░░░░░░░]",
    "Hacking... 56.21%\n[█████████░░░░░░░░░░░]",
    "Hacking... 86.21%\n[███████████████░░░░░]",
    "Hacking... 93.50%\n[█████████████████░░░]",
    "hacking...  100%\n[████████████████████]",
    "hacking... COMPLE. ✅",
]
    for string in range(8):
          await asyncio.sleep(4)
          await message.edit(HACK_STRING[string % 8])
