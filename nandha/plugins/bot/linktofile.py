


import base64
import secrets




from nandha import bot, DATABASE
from nandha.helpers.decorator import devs_only

from pyrogram import filters, types


def gen_token():
    random_hex = secrets.token_hex(16)
    return random_hex
    
def encode(string: str):
    encoded_bytes = base64.b64encode(string.encode('utf-8'))
    return encoded_bytes.decode('utf-8')

def decode(string: str):
    decoded_bytes = base64.b64decode(string.encode('utf-8'))
    return decoded_bytes.decode('utf-8')

db = DATABASE['LINK_TO_FILE']
    
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
            if db.find_one(user_json) and len(message.text.split()) == 2:
                 token = message.text.split(None, 1)[1]
                 ignore = ['_id', 'user_id']
                 user_tokens = [ token for token in db.find_one(user_json) if token not in ignore]
                 if token in user_tokens:
                     db.update_one(
                        user_json, {'$push': {token: file_id}})
                 
                     return await message.reply(
                         '**Successfully file added in token.**',
                   reply_markup=types.InlineKeyboardMarkup(
                       [[types.InlineKeyboardButton('click here', url=link.format(token))]]
                   ))
                 else:
                     return await message.reply(
                         'Sorry. itz not a valid token 🤔')
            else:
                token = gen_token
                db.update_one(
                   {'user_id': user_id},
                   {'$set': {token: [file_id]}},
                   upsert=True
                )                
                return await message.reply(
                   '**Successfully new token generated and added file.**',
                    reply_markup=types.InlineKeyboardMarkup(
                        [[types.InlineKeyboardButton('click here', url=link.format(token))]]
                    ))
       else:
          return await message.reply(
       'Reply to the document file.'
   )
                
