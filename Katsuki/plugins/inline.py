
import config 
import requests


from Katsuki import MODULE, bot, INFO as GET_INFO
from Katsuki.helpers.help_func import spacebin
from pyrogram import filters

from pyrogram.types import (
InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton )


 

@bot.on_inline_query(filters.regex("help"))
async def help_cmds(_, inline_query):
    user_id = (await GET_INFO.app()).id
    if not inline_query.from_user.id == user_id:
        return  
    buttons = [[InlineKeyboardButton(x['module'], callback_data=f"help:{x.get('module')}")] for x in MODULE]
    await bot.answer_inline_query(
      inline_query.id,
      cache_time=0,
      results = [
     InlineQueryResultArticle(
        "🆘 Help Commands",  InputTextMessageContent(message_text="Help Commands!"), thumb_url="https://graph.org/file/b136511bda43b1d8db7d2.jpg",reply_markup=InlineKeyboardMarkup(buttons))])


@bot.on_inline_query(filters.regex("paste"))
async def paste(_, inline_query):
    user_id = (await GET_INFO.app()).id
    if not inline_query.from_user.id == user_id:
       return 
    string = inline_query.query
    try:
       CONTENT = string.split(maxsplit=1)[1]
    except:
       return 
    mm = await spacebin(CONTENT)
    link = mm["result"]["link"]
    raw = mm["result"]["raw"]
    await bot.answer_inline_query(
       inline_query.id,
       cache_time=0,
    results=[
       InlineQueryResultArticle(
            "Paste Success ✅",
            InputTextMessageContent(message_text="BELOW BUTTONS TO VIEW PASTE!", disable_web_page_preview=True), thumb_url="https://graph.org/file/4f71af878a085505e8faf.jpg",
     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("➡️ PASTE", url=link),
       InlineKeyboardButton("➡️ RAW", url=raw)]]))])



