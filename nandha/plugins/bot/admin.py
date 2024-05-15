

from nandha import bot
from nandha.plugins.user.admin import (
delete_msg 
)

from pyrogram.handlers import MessageHandler
import config



bot.add_handler(MessageHandler(delete_msg), config.command('del'))

