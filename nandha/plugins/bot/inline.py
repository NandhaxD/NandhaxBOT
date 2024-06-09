


from pyrogram import filters, types, enums, errors
from nandha import bot, DATABASE
from nandha.plugins.bot.linktofile import get_file_ids_by_token, get_user_tokens



@bot.on_inline_query()
async def inline_query(bot, query: types.InlineQuery):
      data = query.query
      BotInfo = await bot.get_me()
      results = []
      
      if data and data.split()[0] == 'fs':
           if not len(data.split()) == 2:
               tokens = get_user_tokens(query.from_user.id)
               if not tokens:
                   text = "You haven't generate any token it 🐍"
               else:
                   text = f"{query.from_user.first_name}'s Token:\n× " + "\n× ".join(tokens)
               results.append(
                   types.InlineQueryResultArticle(
                        f"✨ View Your Tokens Here.",
                   types.InputTextMessageContent(text))
               )
            
           
           if not results and len(data.split()) == 2:
                 
               token = data.split()[1]
               user_id, file_ids = get_file_ids_by_token(token)
               if not file_ids:  
                    results.append(
                      types.InlineQueryResultArticle(
                        f"❌ Token {token} not found!",
                      types.InputTextMessageContent("The Token You given it's Invalid 🐍"))
                     )
               else:
                   try:
                       name = (await bot.get_users(user_id)).first_name
                   except:
                       name = user_id
                   results.extend([types.InlineQueryResultCachedDocument(title=f"No: {idx}, File by {name}",document_file_id=id) for idx, id in enumerate(file_ids, start=1)])
                   
               await bot.answer_inline_query(
                  inline_query_id=query.id,
                  results=results,
                  switch_pm_text=f"Powered by @{BotInfo.first_name}",
                  switch_pm_parameter="start",
                  cache_time=1
                   )
                    
           
