from telegraph import upload_file, Telegraph
from pyrogram import filters
from Katsuki import app
import config





""" TELEGRAPH MEDIA UPLOADER """

@app.on_message(filters.command("tm", prefixes=config.HANDLER) & filters.me)
async def tm(_, message):
    await message.edit('processing...')
    reply_is = message.reply_to_message
    if not reply_is:
         return await message.edit_text("💔 Reply To The Media!")
    types = [True if reply_is.document else True if reply_is.photo else True if reply_is.animation else False][0]
    if types:
        path = await message.reply_to_message.download()
        grap = upload_file(path)
        for code in grap:
              url = "https://graph.org"+code
        return await message.edit(str(url))



""" TELEGRAPH PAGE CREATOR """

telegraph = Telegraph()
telegraph.create_account(short_name=config.NAME)


@app.on_message(filters.command("txt", prefixes=config.HANDLER))
async def graph_text(_, message):
     
     first_name=message.from_user.first_name
     if len(message.text.split()) >= 2:
           text = message.text.split(maxsplit=1)[1]
     else:
          if (message.reply_to_message and message.reply_to_message.text or message.reply_to_message.caption):
                text = (message.reply_to_message.text or message.reply_to_message.caption)
          else:
              return await message.edit('reply to the text for give some text to upload telegraph')
          response = telegraph.create_page(first_name, html_content=text)
          page_url = response['url']
          return await message.edit(page_url)
