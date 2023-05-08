import asyncio 
import config

from Katsuki import katsuki 
from Katsuki.helpers.help_func import make_carbon
from pyrogram import filters
from gpytranslate import Translator

import requests


@katsuki.on_message(filters.command("carbon", prefixes=config.HANDLER) & filters.user(config.OWNER_ID))
async def make_carbon(_, message):
     REPLY=message.reply_to_message
     if not REPLY:
          if not len(message.text.split()) == 2:
                 return await message.edit('=> `.carbon katsuki`')
          text = message.text.split(maxsplit=1)[1]
     else:
         if not REPLY.text and not REPLY.caption:
               return await message.edit('reply to message text only.')
         text = REPLY.caption or REPLY.caption
     msg = await message.edit('IMAGE GENERATING...')
     IMAGE= await make_carbon(text)
     await message.reply_photo(photo=IMAGE, quote=True)
     return await msg.delete()

@katsuki.on_message(filters.command(["ud","define"],prefixes=config.HANDLER) & filters.user(config.OWNER_ID))
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
        ud = await message.edit_text("Exploring....")
        await ud.edit_text(reply_text)
        
        
trans = Translator()
@katsuki.on_message(filters.command("tr",prefixes=config.HANDLER) & filters.user(config.OWNER_ID))
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
