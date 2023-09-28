"""
Copyright © [2023-2024] @NandhaBots. All rights reserved. Reproduction, modification, distribution, or republication of this file without prior written permission from @NandhaBots is strictly prohibited. The Katsuki Telegram user bot has been developed with the Pyrogram library and utilizing Python programming language, making it a safe and secure option for users. Unauthorized use of this bot or any part of it may result in legal action. This project is owned by @Nandha, and any unauthorized use or distribution of this bot is strictly prohibited.
"""

import config, asyncio, image
from pyrogram import filters
from Katsuki import app

@app.on_message(filters.me & filters.command('alive', prefixes=config.HANDLER))
async def alive(_, message):
    msg = await message.edit('1️⃣0️⃣0️⃣0️⃣0️⃣0️⃣0️⃣0️⃣0️⃣')
    await msg.edit('1️⃣2️⃣0️⃣0️⃣0️⃣0️⃣0️⃣0️⃣0️⃣')
    await asyncio.sleep(2)
    await msg.edit('1️⃣2️⃣3️⃣0️⃣0️⃣0️⃣0️⃣0️⃣0️⃣')
    await asyncio.sleep(2)
    await msg.edit('1️⃣2️⃣3️⃣4️⃣0️⃣0️⃣0️⃣0️⃣0️⃣')
    await asyncio.sleep(2)
    await msg.edit('1️⃣2️⃣3️⃣4️⃣5️⃣0️⃣0️⃣0️⃣0️⃣')
    await asyncio.sleep(2)
    await msg.edit('0️⃣1️⃣2️⃣4️⃣5️⃣6️⃣0️⃣0️⃣0️⃣')
    await asyncio.sleep(2)
    await msg.edit('0️⃣1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣0️⃣')
    await asyncio.sleep(2)
    await msg.edit('0️⃣1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣')
    await asyncio.sleep(2)
    await message.repy_photo(image.ALIVE_IMG, caption=string.ALIVE_IMG)
    await msg.delete()
    
    
  
