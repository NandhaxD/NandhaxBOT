"""
Copyright © [2023-2024] @NandhaBots. All rights reserved. Reproduction, modification, distribution, or republication of this file without prior written permission from @NandhaBots is strictly prohibited. The Katsuki Telegram user bot has been developed with the Pyrogram library and utilizing Python programming language, making it a safe and secure option for users. Unauthorized use of this bot or any part of it may result in legal action. This project is owned by @Nandha, and any unauthorized use or distribution of this bot is strictly prohibited.
"""




import pyrogram
import strings
import config

from Katsuki import bot , app
from Katsuki.helpers.help_func import get_datetime 

async def run_clients():
      await bot.start()
      await app.start()
      await pyrogram.idle()
      zone = await get_datetime()
      await bot.send_message(
           chat_id=config.OWNER_ID,
           text=strings.RESTART_TEXT.format(date=zone["date"], time=zone["time"]))
      


if __name__ == "__main__":
    app.loop.run_until_complete(run_clients())
