import config

from Katsuki import app, bot
from pyrogram import filters




@app.on_message(filters.me & filters.command("help", prefixes=config.HANDLER))
async def help_command(_, message):
      BOT_USERNAME = (await bot.get_me()).username
      query = "help"
      result = await app.get_inline_bot_results(bot=BOT_USERNAME, query=query)
      await app.send_inline_bot_result(chat_id=message.chat.id, query_id=result.query_id, result_id=result.results[0].id, reply_to_message_id=message.id)
      await message.delete()
