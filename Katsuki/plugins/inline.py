
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
    buttons = [[InlineKeyboardButton(x['module'], callback_data=f"help:{x['module']}")] for x in MODULE]
    await bot.answer_inline_query(
      inline_queey.id,
      cache_time=0,
      results = [
     InlineQueryResultArticel(
        "🆘 Help Commands",  InputTextMessageContent(message_text="Help Commands!"),reply_markup=buttons)])


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
            InputTextMessageContent(message_text="BELOW BUTTONS TO VIEW PASTE!", disable_web_page_preview=True),
     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("➡️ PASTE", url=link),
       InlineKeyboardButton("➡️ RAW", url=raw)]]))])



