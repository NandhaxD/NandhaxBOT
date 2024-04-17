
import config 
import requests

from nandha import bot, lang
from nandha.helpers.misc import article
from nandha.helpers.help_func import spacebin
from urllib.parse import quote

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


api_url = 'https://nandha-api.onrender.com/'
error_img = 'https://graph.org/file/6248cbb1e09af24a646f4.jpg'




async def inline_sof(bot, inline_query_id, query):
     try:

         results = []
         context = quote(query.split(None, 1)[1])
         end_point = f'stackoverflow?query={context}'
         req = requests.get(api_url+end_point).json()
         for xx in req['results']:
              button = [[ InlineKeyboardButton(text="Link 🔗", url=xx['link']) ]]
              results.append(
                  await article(
                      name=xx['text'], 
                      article=f"[{xx['text']}]({xx['link']})", 
                      thumb_url="https://graph.org/file/4a9b862e7877aef3ee553.jpg", 
                      
                  )[0] 
              )
         
         await bot.answer_inline_query(
                 inline_query_id, results,
                 cache_time=1
         )
    
     except Exception as e:
             results = await article('ERROR 404',
                        lang['error'].format(e), error_img)
                                    
             await bot.answer_inline_query(
                 inline_query_id,results,
               cache_time=1
              
         )

                  
    

async def inline_paste(bot, inline_query_id, query):
    try:
        context = query.split(None, 1)[1]
        paste = await spacebin(context)
        link = paste['result']['link']
        raw = paste['result']['raw']
        datetime = paste['result']['datetime']
        name = 'Here your paste'
        results = await article(
            name, lang['paste'].format(link, raw, datetime), 'https://graph.org/file/d7ee801a941e632db40f1.jpg')
        
        await bot.answer_inline_query(
                 inline_query_id, results,
               cache_time=1 )
    except Exception as e:
            results = await article('ERROR 404',
                        lang['error'].format(e), error_img)
                                    
            await bot.answer_inline_query(
                 inline_query_id,results,
               cache_time=1
              
            )
    
  


async def inline_fonts(bot, inline_query_id, query):
            try:
                context = query.split(None, 1)[1]
                end_point = f'styletext?query={quote(context)}'
                req = requests.get(api_url+end_point).json()
                context = f"**Query**: {context}\n\n"
                for text in req['fonts']:
                       context += text+"\n"
                results = await article('Style Fonts', context, 'https://graph.org/file/d95f726d8fe3706cc69ae.jpg')
                await bot.answer_inline_query(
                      inline_query_id,results,
                             cache_time=1,
                          
                         )
            except Exception as e:
                    results = await article('ERROR 404',
                        lang['error'].format(e), error_img)
                                    
                    await bot.answer_inline_query(
                 inline_query_id, results,
               cache_time=1,
              
                    )

