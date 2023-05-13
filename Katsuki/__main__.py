import pyrogram
import strings
 
from Katsuki import bot , app
from Katsuki.helpers.help_func import get_datetime 

async def run_clients():
      await bot.start()
      await app.start()
      await pyrogram.idle()
      zone = await get_datetime()
      await bot.send_message(
           chat_id=config.GROUP_ID,
           text=strings.RESTART_TEXT.format(zone["date"], zone["time"])
      


if __name__ == "__main__":
    app.loop.run_until_complete(run_clients())
