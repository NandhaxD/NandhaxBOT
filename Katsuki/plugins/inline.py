
import config 

from Katsuki import app
from Katsuki.helpers.help_func import spacebin
from pyrogram import filters

from pyrogram.types import (
InlineQueryResultArticle, InputTextMessageContent )

@app.on_inline_query(filters.regex("paste") & filters.user(config.OWNER_ID))
async def hello(_, inline_query):
    string = inline_query.query
    STRING = string.split(maxsplit=2)[2]
    MMMM = await spacebin(STRING)
    await app.answer_inline_query(
       inline_query.id,
       cache_time=0,
    results=[
       InlineQueryResultArticle(
            "Here the Is The Paste!",
            InputTextMessageContent(message_text=MMMM, disable_web_page_preview=True))])

