
import config 
import requests


from Katsuki import app
from Katsuki.helpers.help_func import spacebin
from pyrogram import filters

from pyrogram.types import (
InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton )

from pyrogram.raw.types import KeyboardButtonSwitchInline






@app.on_inline_query(filters.regex("run") & filters.user(config.OWNER_ID))
async def run_code(_, inline_query):
     string = inline_query.query
     language = string.split()[2]
     code = string.split(maxsplit=3)[1]
     url = 'https://api.codex.jaagrav.in'
     payload = {
       'code': code,
       'language': language,
       'input': ''}
     response = requests.post(url, data=payload)
     if response.ok:
          result=response.json()
          language=result['language']
          info=result['info']
          errors=result['error']
          output=result['oupput']
          text = "**🖥️ Code**:\n"
          text += f"`{code}`"
          text += f"⌨️ **Language**: `{info}`"
          if errors:
              text += f"**Output**:\n`{errors}`"
          else:
              text += f"**Output**:\n`{output}`"
          share=f"t.me/share?text={text}"
          return await app.answer_inline_query(
       inline_query.id,
       cache_time=0,
    results=[
       InlineQueryResultArticle(
            "💥 Results 💥",
            InputTextMessageContent(message_text="BELOW BUTTONS TO VIEW PASTE!", disable_web_page_preview=True),
     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("➡️ Share", url=share)]]))])




@app.on_inline_query(filters.regex("paste") & filters.user(config.OWNER_ID))
async def paste(_, inline_query):
    string = inline_query.query
    try:
       CONTENT = string.split(maxsplit=2)[1]
    except:
       return 
    mm = await spacebin(CONTENT)
    link = mm["result"]["link"]
    raw = mm["result"]["raw"]
    await app.answer_inline_query(
       inline_query.id,
       cache_time=0,
    results=[
       InlineQueryResultArticle(
            "✅ Paste Success ✅",
            InputTextMessageContent(message_text="BELOW BUTTONS TO VIEW PASTE!", disable_web_page_preview=True),
     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("➡️ PAST", url=link),
       InlineKeyboardButton("➡️ RAW", url=raw)]]))])

