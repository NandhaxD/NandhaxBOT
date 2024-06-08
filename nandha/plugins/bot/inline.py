


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
      data = query.query
      results = []
      if data and data.split()[0] == 'fs':
           if not len(data.split()) == 2:
                return
           token = data.split()[1]
           file_ids = await get_token_file_ids(token)
           if not file_ids:
               results.append(
                   types.InlineQueryResultArticle(
                        f"❌ Token {token} not found!",
                   types.InputTextMessageContent("The Token You given it's Invalid 🐍"))
                  )
           else:
               results.extend([types.InlineQueryResultCachedDocument(title=f"File: {idx}",document_file_id=id) for idx, id in enumerate(file_ids, start=1)])
              
      await bot.answer_inline_query(
             inline_query_id=query.id,
             results=results,
             switch_pm_text=f"Total Results: {len(results)}",
             switch_pm_parameter="start",
             cache_time=1
      )
                    
           
