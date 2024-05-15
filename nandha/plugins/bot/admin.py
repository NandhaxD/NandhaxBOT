

from nandha import bot
from nandha.plugins.user.admin import (
delete_msg, purge_msg
)

from pyrogram.handlers import MessageHandler
import config



bot.add_handler(MessageHandler(delete_msg, filters.command('del')))
bot.add_handler(MessageHandler(purge_msg, filters.command('purge')))

