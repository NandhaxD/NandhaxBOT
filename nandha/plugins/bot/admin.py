

from nandha import bot
from nandha.plugins.user.admin import (
delete_msg 
)

from pyrogram import filters
from pyrogram.handlers import MessageHandler
import config



bot.add_handler(delete_msg, config.command('del'))

