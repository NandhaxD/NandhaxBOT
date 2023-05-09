
import config 

from Katsuki import app
from Katsuki.helpers.help_func import spacebin
from pyrogram import filters

from pyrogram.types import (
InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton )

from pyrogram.raw.types import KeyboardButtonSwitchInline

def error_inline_query(app, inline_query, text):
     Inline = await app.answer_inline_query(
     inline_query.id,
     cache_time=0,
     results = [
        InlineQueryResultArticle(
           "🥴 Somthing wrong Happens!",
        InputTextMessageContent(text), disable_web_page_preview=True,
         reply_markup=InlineKeyboardMarkup([[KeyboardButtonSwitchInline(text="TAP 👈", query=text),]]))])
     return inline
            

@app.on_inline_query(filters.regex("paste") & filters.user(config.OWNER_ID))
async def paste(_, inline_query):
    string = inline_query.query
    try:
       STRING = string.split(maxsplit=2)[1]
    except:
        await error_inline_query(app=app, inline_query=inline_query, text="paste hello")
    mm = await spacebin(STRING)
    link = mm["result"]["link"]
    raw = mm["result"]["raw"]
    await app.answer_inline_query(
       inline_query.id,
       cache_time=0,
    results=[
       InlineQueryResultArticle(
            "Here the Is The Paste!",
            InputTextMessageContent(message_text="BELOW BUTTONS TO VIEW PASTE!", disable_web_page_preview=True),
     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("➡️ PAST", url=link),
       InlineKeyboardButton("➡️ RAW", url=raw)]]))])

