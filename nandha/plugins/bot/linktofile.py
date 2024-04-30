


import base64


from nandha import bot, DATABASE
from nandha.helpers.decorator import devs_only

from pyrogram import filters, types

def encode(string: str):
    encoded_bytes = base64.b64encode(string.encode('utf-8'))
    return encoded_bytes.decode('utf-8')

def decode(string: str):
    decoded_bytes = base64.b64decode(string.encode('utf-8'))
    return decoded_bytes.decode('utf-8')
    
    
link = 'nandhaxbot.t.me?start=file:{}'    

@bot.on_message(filters.command('getlink'))
@devs_only
async def Getlink(_, message):
       user_id = message.from_user.id
       reply = message.reply_to_message
       document = reply.document if reply and reply.document else False
       if document:
            file_id = document.file_id
            user_json = {'user_id': user_id}
            if db.find_one(user_json):
                 db.update_one(
                   {'$push': {'file_ids': file_id}})
                 id = encode(file_id)
                 return await message.reply(
                   'Successfully added', reply_markup=types.InlineKeyboardMarkup([[types.InlineKeyboardButton('click here', url=link.format(id))]]))
            else:
                file_json = {'file_ids' [file_id]}
                new_user_json = user_json.update(file_json)
                db.insert_one(new_user_json
                  )
                id = encode(file_id)
                return await message.reply(
                   'Successfully added', reply_markup=types.InlineKeyboardMarkup([[types.InlineKeyboardButton('click here', url=.format(id))]]))
