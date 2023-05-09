import config 

from Katsuki import app
from pyrogram import filters

from pyrogram.types import (
InlineQueryResultArticle, InputTextMessageContent )

@app.on_inline_query(filters.regex("hello") & filters.user(config.OWNER_ID))
async def hello(_, inline_query):
    await app.answer_inline_query(
       inline_query.id,
       cache_time=0,
    results=[
       InlineQueryResultArticle(
            "Here the Is The Help!",
            InputTextMessageContent('hello master 😘'))])

