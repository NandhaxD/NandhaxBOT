
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
        "🆘 HELP COMMANDS",  InputTextMessageContent(message_text="HELP COMMANDS!"), thumb_url="https://graph.org/file/b136511bda43b1d8db7d2.jpg",reply_markup=InlineKeyboardMarkup(buttons))])


@bot.on_inline_query(filters.regex("test"))
async def test(_, inline_query):
    user_id = (await GET_INFO.app()).id
    if not inline_query.from_user.id == user_id:
       return 
    string = inline_query
    await bot.answer_inline_query(
       inline_query.id,
       cache_time=0,
    results=[
       InlineQueryResultArticle(
            "Here the InlineQuery Objecs",
            InputTextMessageContent(message_text=string, disable_web_page_preview=True), thumb_url="https://graph.org/file/4f71af878a085505e8faf.jpg")])
     

