


from pyrogram import filters, types, enums, errors
from nandha import bot, DATABASE



async def get_token_file_ids(token: str):
    db = DATABASE['LINK_TO_FILE']
    file_ids = []
    for tokens in db.find():
       if token in tokens:
          user_id = tokens['user_id']
          file_ids = tokens[token]
          return file_ids
    return file_ids
     
        
           



@bot.on_inline_query()
async def inline_query(bot, query: types.InlineQuery):
      data = query.query.lower()
      results = []
      if data and data.split()[0] == 'fs':
           if not len(data.split()) == 2:
                return
           token = data.split()[1]
           file_ids = get_token_file_ids(token)
           if not file_ids:
               results.append(
                   types.InlineQueryResultArticle(
                        f"❌ Token {token} not found!",
                   types.InputTextMessageContent("The Token You given it's Invalid 🐍"))
                  )
           else:
               file_ids = get_token_file_ids(token)
               results.extend([types.InlineQueryResultCachedDocument(document_file_id=id) for id in file_ids])
              
      await bot.answer_inline_query(
             inline_query_id=query.id,
             results=results,
             switch_pm_text=f"Total Results: {len(results)}",
             switch_pm_parameter="start",
             cache_time=1
      )
                    
           
