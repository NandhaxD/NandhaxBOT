


from pyrogram import filters, types, enums, errors
from nandha import bot, DATABASE
from nandha.plugins.bot.linktofile import get_file_ids_by_token



@bot.on_inline_query()
async def inline_query(bot, query: types.InlineQuery):
      data = query.query
      results = []
      if data and data.split()[0] == 'fs':
           if not len(data.split()) == 2:
                return
           token = data.split()[1]
           user_id, file_ids = get_file_ids_by_token(token)
           if not file_ids:
               results.append(
                   types.InlineQueryResultArticle(
                        f"❌ Token {token} not found!",
                   types.InputTextMessageContent("The Token You given it's Invalid 🐍"))
                  )
           else:
               user = await bot.get_user(user_id)
               results.extend([types.InlineQueryResultCachedDocument(title=f"No: {idx} File by {user.first_name}",document_file_id=id) for idx, id in enumerate(file_ids, start=1)])
              
      await bot.answer_inline_query(
             inline_query_id=query.id,
             results=results,
             switch_pm_text=f"Total Results: {len(results)}",
             switch_pm_parameter="start",
             cache_time=1
      )
                    
           
