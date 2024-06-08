


from pyrogram import filters, types, enums, errors
from nandha import bot, DATABASE



def check_token(token: str):
   db = DATABASE['LINK_TO_FILE']
   file_ids = []
   for tokens in db.find():
      if token in tokens:
          user_id = tokens['user_id']
          file_ids = tokens[token]
   return file_ids
           



@bot.on_inline_query()
async def inline_query(bot, query: types.InlineQuery):
      query = query.query.lower()
      results = []
      if query.split()[0] == 'fs':
           if not len(query.split()) == 2:
                return
           token = query.split()[1]
           if not check_token(token):
               results.append(
                   types.InlineQueryResultArticle(
                        "❌ Token Not found!",
                   types.InputTextMessageContent("The Token You given it's Invalid 🐍"))
                  )
           else:
               print('ok')
                
                    
           
