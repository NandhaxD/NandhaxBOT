
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent


async def article(name: str, article: str, thumb_url: str , keyboard: str = None):     
     results=[
         InlineQueryResultArticle(
                   name,
                     InputTextMessageContent(
                message_text=article,
                               disable_web_page_preview=True), 
             thumb_url=thumb_url, 
             reply_markup=keyboard
         )
     ]
     return results
