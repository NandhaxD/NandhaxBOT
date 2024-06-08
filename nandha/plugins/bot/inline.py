


from pyrogram import filters, types, enums, errors
from nandha import bot, DATABASE



def get_token_file_ids(token: str):
   db = DATABASE['LINK_TO_FILE']
   file_ids = []
   for tokens in db.find():
      if token in tokens:
          user_id = tokens['user_id']
          file_ids = tokens[token]
   return file_ids
           



@bot.on_inline_query()
async def inline_query(bot, query: types.InlineQuery):
      data = query.query.lower()
      results = []
      if data.split()[0] == 'fs':
           if not len(data.split()) == 2:
                return
           token = data.split()[1]
           if not get_token_file_ids(token):
               results.append(
                   types.InlineQueryResultArticle(
                        "❌ Token Not found!",
                   types.InputTextMessageContent("The Token You given it's Invalid 🐍"))
                  )
           else:
               file_ids = get_token_file_ids(token)
               results.extend([types.InlineQueryResultCachedDocument(document_file_id=id) for id in file_ids])
              
      await bot.answer_inline_query(
             inline_query_id=query.id,
             results=results,
             switch_pm_text=f"Total file in token: {len(results)}",
             switch_pm_parameter="start",
             cache_time=2
      )
                    
           
