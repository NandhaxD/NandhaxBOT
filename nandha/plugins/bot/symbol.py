import json
from pyrogram import types, filters
from nandha import bot

# Load the data from the JSON file

with open("./nandha/helpers/database/symbols_data.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)



@bot.on_message(filters.command('symbols'))
async def symbols(_, message):

     chat_id = message.chat.id
     buttons = []
     for index, ( title, content) in enumerate(data.items()):
          if index >= 4:
               break
          buttons.append(
            types.InlineKeyboardButton(
            title, callback_data=f'symbol:{index}'
        )
    )
     columns_btn = [ [button] for button in buttons ]
     reply_markup = types.InlineKeyboardMarkup(columns_btn)

     return await bot.send_message(
             chat_is=chat_id, text='Here the list of symbols, i hope you can find something awesome.',
             reply_markup=reply_markup)


             

