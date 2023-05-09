import config 

from Katsuki import app
from pyrogram import filters

from pyrogram.types import InlineQueryResultArticle

@app.on_inline_query(filters.regex("hello") & filters.user(config.OWNER_ID))
async def hello(_, query):
    await app.answer_inline_query(
       query.id,
    results=[
       InlineQueryResultArticle(
            "Here the Is The Help!",
            InputTextMessageContent('hello master 😘'))])

