import json
from pyrogram import types, filters
from nandha import bot

# Load the data from the JSON file

with open("./nandha/helpers/database/symbols_data.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)

num_columns = 8

@bot.on_message(filters.command('symbols'))
async def symbols(_, message):

     chat_id = message.chat.id
     user_id = message.from_user.id
    
     buttons = []
     for index, ( title, content) in enumerate(data.items()):
          if index >= 5:
               break
          buttons.append(
            types.InlineKeyboardButton(
            title, callback_data=f'symbol:{user_id}:{index}'
        )
    )
     columns_btn = [ [button] for button in buttons ]
     reply_markup = types.InlineKeyboardMarkup(columns_btn)

     return await bot.send_message(
             chat_id=chat_id, text='Here the list of symbols, i hope you can find something awesome.',
             reply_markup=reply_markup)



@bot.on_callback_query(filters.regex('^symbol'))
async def cb_symbols(_, query):
    user_id = int(query.data.split(':')[1])
    target_index = int(query.data.split(':')[2])
    if query.from_user.id != user_id:
          return await message.reply(
              'Sorry, this is not your Query.')
    text = ''
    for index, (title, content) in enumerate(data.items()):
       if index == target_index:
           text += f'**{title}**:\n\n'
           for i in range(0, len(content), num_columns):
                 text += ' '.join(content[i:i + num_columns])
           break
    return await query.message.edit(text)
    



