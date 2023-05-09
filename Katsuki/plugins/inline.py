import config 

from Katsuki import app
from pyrogram import filters


@app.on_inline_query(filters.regex("hello") & filters.user(config.OWNER_ID))
async def hello(_, query):
    await client.answer_inline_query(
       query.id,
    results=[
       InlineQueryResultArticle(
            "Here the Is The Help!",
            InputTextMessageContent('hello master 😘'))])
)
