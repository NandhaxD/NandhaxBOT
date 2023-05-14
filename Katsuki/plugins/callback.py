
import strings

from Katsuki import bot, MODULE, INFO as GET_INFO
from pyrogram import filters, enums 

from pyrogram.types import ( 
InlineKeyboardMarkup, InlineKeyboardButton )


@bot.on_back_query(filters.regex("help_back"))
async def help_back(_, query):
   user_id = (await GET_INFO.app()).id
   if not query.from_user.id == int(user_id):
       return await query.answer("😤 You aren't my master")
       buttons = [[InlineKeyboardButton(x['module'], callback_data=f"help:{x.get('module')}")] for x in MODULE]
       return bot.edit_inline_text(
        inline_message_id, query.inline_message_id,
       
     

@bot.on_callback_query(filters.regex('^help'))
async def help_commnds(_, query):
   user_id = (await GET_INFO.app()).id
   if not query.from_user.id == int(user_id):
       return await query.answer("😤 You aren't my master")
   CB_NAME = query.data.split(':')[1].casefold()
   data = [x for x in MODULE if x['module'].casefold() == CB_NAME]
   if len(data) == 0:
       return await query.answer("🤔 somthing wrong.")
   module = data[0]['module']
   help = data[0]['help']
   return await bot.edit_inline_text(inline_message_id=query.inline_message_id, text=strings.HELP_CMD.format(module=module, help=help), parse_mode=enums.ParseMode.MARKDOWN)
       
            
            

   
