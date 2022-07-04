from Katsuki import katsuki 
from config import OWNER_ID, HANDLER
from pyrogram import filters
from gpytranslate import Translator

import requests

@katsuki.on_message(filters.command("ud",prefixes=HANDLER) & filters.user(OWNER_ID))
async def ud(_, message):
        if len(message.command) < 2:
             await message.reply("ɢɪᴠᴇ ᴍᴇ ᴀ ᴛᴇxᴛ")
             return
        text = message.text.split(None, 1)[1]
        results = requests.get(
        f'https://api.urbandictionary.com/v0/define?term={text}').json()
        reply_text = f'**results: {text}**\n\n{results["list"][0]["definition"]}\n\n_{results["list"][0]["example"]}_'
        ud = await message.reply_text("ғɪɴᴅɪɴɢ.. ᴅᴇғɪɴᴇ.")
        await ud.edit_text(reply_text)
        
        
trans = Translator()


@katsuki.on_message(filters.command("tr",prefixes=HANDLER) & filters.user(OWNER_ID))
async def translate(_, message) -> None:
    reply_msg = message.reply_to_message
    if not reply_msg:
        await message.reply_text("[ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴛʀᴀɴsʟᴀᴛᴇ ɪᴛ!](https://telegra.ph/Lang-Codes-03-19-3)")
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
