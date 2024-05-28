


import base64
import secrets




from nandha import bot, DATABASE
from nandha.helpers.decorator import devs_only

from pyrogram import filters, types

db = DATABASE['LINK_TO_FILE']
    
link = 'nandhaxbot.t.me?start=getfile-{}'    


#def gen_token():
#    random_hex = secrets.token_hex(16)
 #   return random_hex

def gen_token(length=10):
    # Define the characters to choose from (letters and digits only)
    characters = string.ascii_letters + string.digits
    # Generate a random string using list comprehension
    random_string = ''.join([random.choice(characters) for _ in range(length)])
    return random_string
    
def encode(string: str):
    encoded_bytes = base64.b64encode(string.encode('utf-8'))
    return encoded_bytes.decode('utf-8')

def decode(string: str):
    decoded_bytes = base64.b64decode(string.encode('utf-8'))
    return decoded_bytes.decode('utf-8')


def delete_file(user_id, token, index):
    result = db.update_one({'user_id': user_id}, {'$pull': {key: index}})
    return result.modified_count == 1


def get_user_tokens(user_id):
    user_data = db.find_one({'user_id': user_id})
    if user_data:
        tokens_with_count = [(key, len(value)) for key, value in user_data.items() if key not in ['_id', 'user_id']]
        return tokens_with_count
    return None


def delete_token(user_id, token):
    result = db.update_one(
        {'user_id': user_id},
        {'$unset': {token: ""}}
    )
    return result.modified_count > 0

      
@bot.on_message(filters.command(['clearfile','cfile']))
@devs_only
async def clear_file(_, message):
     m = message
     r = message.reply_to_message

     usage = "❌ Give the token with number `/cfile token 0`"
  
     if len(message.command) == 3:
          token = m.text.split()[1]
          try:
             file_id = int(m.text.split()[2])-1
          except ValueError:
             return await m.reply_text(
               text=usage
) 
     else:
         return await m.reply_text(
             text=usage
         )
      
     user_id = m.from_user.id
     
     if delete_file(user_id, token, file_id):
          return await m.reply_text(
               f"⛔ File deleted from token {token}"
                                       )
     else:
          return await m.reply_text(
                "❌ File doesn't exsit in Token."
              )             


@bot.on_message(filters.command(['cleartoken','ctoken']))
@devs_only
async def clear_token(_, message):
     m = message
     if len(message.command) != 2:
          return await m.reply_text("Ok! but where token to delete?")
     else:
          user_id = m.from_user.id
          if delete_token(user_id, m.text.split()[1]):
              return await m.reply_text(
                  "Token deleted!"
                                       )
          else:
              return await m.reply_text(
                  "Token doesn't exsit in database."
              )         
                
@bot.on_message(filters.command(['gettokens', 'gettk']))
@devs_only
async def GetTokens(_, message):
     user_id = message.from_user.id
     tokens = get_user_tokens(user_id)
     String = f"**🌟 Stored tokens in {message.from_user.mention}**:\n"
     for i, (token, file) in enumerate(tokens):
          String += f"{i+1}, `{token}`: **{file}**\n"
     return await message.reply_text(
           text=String, quote=True
     )



         

@bot.on_message(filters.command(['addfile', 'getlink']))
@devs_only
async def Getlink(_, message):
       user_id = message.from_user.id
       reply = message.reply_to_message
       file = reply.document or reply.video if reply and reply.document or reply.video else False

       if file:
        
            file_id = file.file_id
            user_json = {'user_id': user_id}
            if db.find_one(user_json) and len(message.text.split()) == 2:
                 token = message.text.split(None, 1)[1]
                 ignore = ['_id', 'user_id']
                 user_tokens = [ token for token in db.find_one(user_json) if token not in ignore]
                 if token in user_tokens:
                     db.update_one(
                        user_json, {'$push': {token: file_id}})
                 
                     return await message.reply(
                         f'**Successfully file added in token.**\n**🌟 Token**: `{token}`',
                   reply_markup=types.InlineKeyboardMarkup(
                       [[types.InlineKeyboardButton('Click here', url=link.format(token))]]
                   ))
                 else:
                     return await message.reply(
                         'Sorry. itz not a valid token 🤔')
            else:
                token = gen_token()
                db.update_one(
                   {'user_id': user_id},
                   {'$set': {token: [file_id]}},
                   upsert=True
                )                
                return await message.reply(
                   f'**Successfully new token generated and added file.**\n**🌟 Token**: `{token}`',
                    reply_markup=types.InlineKeyboardMarkup(
                        [[types.InlineKeyboardButton('click here', url=link.format(token))]]
                    ))
       else:
          return await message.reply(
       'Reply to the document file.'
   )
                
