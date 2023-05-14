
import config 
import requests


from Katsuki import app
from Katsuki.helpers.help_func import spacebin
from pyrogram import filters

from pyrogram.types import (
InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton )


@bot.on_inline_query(filters.regex("paste") & filters.me)
async def paste(_, inline_query):
    string = inline_query.query
    try:
       CONTENT = string.split(maxsplit=2)[1]
    except:
       return 
    mm = await spacebin(CONTENT)
    link = mm["result"]["link"]
    raw = mm["result"]["raw"]
    buttons = [[
       InlineKeyboardButton("➡️ PASTE", url=link),
       InlineKeyboardButton("➡️ RAW", url=raw)]]
    await app.answer_inline_query(
       inline_query.id,
       cache_time=0,
    results=[
       InlineQueryResultArticle(
            title="Paste Success ✅",
            thumb_url="https://graph.org/file/1cad98a3f492adba64650.jpg",
            InputTextMessageContent(message_text="BELOW BUTTONS TO VIEW PASTE!", disable_web_page_preview=True),
     reply_markup=InlineKeyboardMarkup(buttons))])


