import re
import time
import importlib

from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto

from nandha import bot
from nandha.helpers.misc import paginate_modules
from nandha.plugins.bot import ALL_MODULES


HELPABLE = {}

def get_helps():
    global HELPABLE
    for module in ALL_MODULES:
        try:
            imported_module = importlib.import_module("nandha.plugins.bot." + module)
            if (
                hasattr(imported_module, "__module__")
                and imported_module.__module__
            ):
                imported_module.__module__ = imported_module.__module__
                if (
                    hasattr(imported_module, "__help__")
                    and imported_module.__help__
                ):
                    HELPABLE[
                        imported_module.__module__.replace(" ", "_").lower()
                    ] = imported_module
        except Exception as e:
            pass
            
get_helps()

async def help_parser(module=None, keyboard=None):
    if not keyboard:
        if module:
            keyboard = InlineKeyboardMarkup(
                [[InlineKeyboardButton("〔 Back 〕", callback_data="help_back")]]
            )
        else:
            keyboard = InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help"))
    if module:
        if module in HELPABLE:
            return (
                f"**Here Is The Help For The** ` {HELPABLE[module].__module__} `**:**\n\n{HELPABLE[module].__help__ or 'No Help Available.'}",
                InlineKeyboardMarkup([[InlineKeyboardButton(" Back ", callback_data="help_back")]]
            ))
    return ("""
ok
""", keyboard)

@bot.on_message(filters.command('help'))
async def _help(_, m: Message):
    module_name = m.text.split()[1] if len(m.text.split()) == 2 else None
    if module_name:
        if module_name in HELPABLE:
            text, keyboard = await help_parser(module_name)
        else:
            text, keyboard = await help_parser()
    else:
        text, keyboard = await help_parser()

    return await m.reply_photo(
        
        text=text,
        reply_markup=keyboard
    )
    
@bot.on_callback_query(filters.regex("bot_commands"))
async def commands_callbacc(_, cq):
  text, keyboard = await help_parser()
  await cq.message.edit_media(
    media=InputMediaPhoto(
      "https://graph.org/file/e026f18e67b056d625c82.jpg",
      caption=text
    ),
    reply_markup=keyboard
  )
  return await bot.answer_callback_query(cq.id)

@bot.on_callback_query(filters.regex(r"help_(.*?)"))
async def help_button(_, cq):
  home_match = re.match(r"help_home\((.+?)\)", cq.data)
  mod_match = re.match(r"help_module\((.+?)\)", cq.data)
  prev_match = re.match(r"help_prev\((.+?)\)", cq.data)
  next_match = re.match(r"help_next\((.+?)\)", cq.data)
  back_match = re.match(r"help_back", cq.data)
  create_match = re.match(r"help_create", cq.data)
  top_text = """
ok
"""
  if mod_match:
    module = (mod_match.group(1)).replace(" ", "_")
    text = (
        "**{}** `{} `:\n".format(
          "Here Is The Help For The", HELPABLE[module].__module__
        )
        + HELPABLE[module].__help__
    )

    await cq.message.edit_caption(
      caption=text,
      reply_markup=InlineKeyboardMarkup(
        [[InlineKeyboardButton("〔 Back 〕", callback_data="help_back")]]
      )
    )
  elif home_match:
    await cq.message.edit_media(
      media=InputMediaPhoto(start_pic, caption=final_txt),
      reply_markup=start_keyboard
    )
  elif prev_match:
    curr_page = int(prev_match.group(1))
    await cq.message.edit_caption(
      caption=top_text,
      reply_markup=InlineKeyboardMarkup(
        paginate_modules(curr_page - 1, HELPABLE, "help")
      )
    )

  elif next_match:
    next_page = int(next_match.group(1))
    await cq.message.edit_caption(
      caption=top_text,
      reply_markup=InlineKeyboardMarkup(
        paginate_modules(next_page + 1, HELPABLE, "help")
      )
    )

  elif back_match:
    await cq.message.edit_caption(
      caption=top_text,
      reply_markup=InlineKeyboardMarkup(
        paginate_modules(0, HELPABLE, "help")
      )
    )

  elif create_match:
    text, keyboard = await help_parser()
    await cq.message.edit_caption(
      caption=text,
      reply_markup=keyboard
    )

  return await bot.answer_callback_query(cq.id)
